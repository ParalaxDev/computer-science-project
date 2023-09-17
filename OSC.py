import socket, struct, math, threading, select, time, queue, osctypes, log
from utils import PadString, DbToFloat, FloatToDb

class OSC:
    def __init__(self, ip, port=10023, host=10024, timeout=5) -> None:
        self.IP = ip
        self.PORT = port
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.SOCK.bind((self.IP, host))
        self.SOCK.setblocking(0)
        self.HOST = host
        self.TIMEOUT = timeout
        self.QUEUE = queue.Queue()

    def setIP(self, newIP):
        self.IP = newIP

    def send(self, OSCMessage: 'ConstructOSCMessage') -> None:

        if OSCMessage.MESSAGE[0] != '/':
            raise Exception('Message must start with /')

        log.info(f"SENDING MESSAGE: {OSCMessage.MESSAGE} {OSCMessage.VALUE_ARRAY}")
        
        self.SOCK.sendto(bytes(PadString(OSCMessage.MESSAGE) + PadString(',' + OSCMessage.TYPE_STRING), 'ascii') + OSCMessage.VALUE_ARRAY, (self.IP, self.PORT))

        if OSCMessage.VALUE_ARRAY == b'':
            return self.receive(OSCMessage, self.decode)
        else:
            return

    def receive(self, msg: 'ConstructOSCMessage', callback):
        ready = select.select([self.SOCK], [], [], 5)

        if ready[0]:
            data, addr = self.SOCK.recvfrom(self.HOST)

            log.info(f"RECEIVED MESSAGE: {data} {addr[0]}")

            m, _ =  [e for e in data.split(b',') if e]

            m = m.strip(b'\x00').decode('ascii')

            if m == msg.MESSAGE:
                res = callback(data)
                return res
            else:
                raise Exception('Observed wrong packet')

    def decode(self, data):

        _, dgram =  [b',' + e for e in data.split(b',') if e]

        typetag, index = osctypes.get_string(dgram, 0)

        params = ()

        if typetag.startswith(','):
            typetag = typetag[1:]

        for type in typetag:
            match type:
                case 'i':
                    val, index = osctypes.get_int(dgram, index)
                case 'f':
                    val, index = osctypes.get_float(dgram, index)
                case 's':
                    val, index = osctypes.get_string(dgram, index)
                case 'b':
                    val, index = osctypes.get_blob(dgram, index)

            params += (val,)

        return params
        

class ConstructOSCMessage:
    def __init__(self, message, args = []) -> None:
        self.MESSAGE = message
        self.TYPE_STRING = ''
        self.VALUE_ARRAY = bytearray()
        for arg in args:
            ty = list(arg.keys())[0]
            self.TYPE_STRING += ty
            val = arg.get(ty)
            match ty:
                case 'f':
                    self.VALUE_ARRAY += bytearray(struct.pack(">f", val))
                case 'i':
                    self.VALUE_ARRAY += bytearray(struct.pack(">i", val))
                case 's':
                    self.VALUE_ARRAY += bytes(PadString(val), 'ascii')
