import socket, select, queue, osc
import utils
from osc import types

class Controller:
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
        # TODO: ip validation
        self.IP = newIP

    def send(self, OSCMessage: osc.construct) -> None:

        if OSCMessage.MESSAGE[0] != '/':
            raise Exception('Message must start with /')

        utils.log.info(f"SENDING MESSAGE: {OSCMessage.MESSAGE} {OSCMessage.VALUE_ARRAY}")
        
        self.SOCK.sendto(bytes(utils.pad(OSCMessage.MESSAGE) + utils.pad(',' + OSCMessage.TYPE_STRING), 'ascii') + OSCMessage.VALUE_ARRAY, (self.IP, self.PORT))

        if OSCMessage.VALUE_ARRAY == b'':
            return self.receive(OSCMessage, self.decode)
        else:
            return

    def receive(self, msg: osc.construct, callback):
        ready = select.select([self.SOCK], [], [], 5)

        if ready[0]:
            data, addr = self.SOCK.recvfrom(self.HOST)

            utils.log.info(f"RECEIVED MESSAGE: {data} {addr[0]}")

            m, _ =  [e for e in data.split(b',') if e]

            m = m.strip(b'\x00').decode('ascii')

            if m == msg.MESSAGE:
                res = callback(data)
                return res
            else:
                utils.log.error('Unexpected packet')
                raise Exception('Observed wrong packet')
        else:
            utils.log.error('Connection timed out')
            return (0, )

    def decode(self, data):

        _, dgram =  [b',' + e for e in data.split(b',') if e]

        typetag, index = types.get_string(dgram, 0)

        params = ()

        if typetag.startswith(','):
            typetag = typetag[1:]

        for type in typetag:
            match type:
                case 'i':
                    val, index = types.get_int(dgram, index)
                case 'f':
                    val, index = types.get_float(dgram, index)
                case 's':
                    val, index = types.get_string(dgram, index)
                case 'b':
                    val, index = types.get_blob(dgram, index)

            params += (val,)

        return params