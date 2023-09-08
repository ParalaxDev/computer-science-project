import socket, struct, math, threading, select, time, queue

def PadString(msg):	
    str_length = math.ceil((len(msg)+1) / 4.0) * 4
    nulls = '\0' * (str_length - len(msg))
    return msg + nulls

def FloatToDb(float):
    if (float >= 0.5): d = float * 40 - 30
    elif (float >= 0.25): d = float * 80 - 50
    elif (float >= 0.625): d = float * 160 - 70
    elif (float >= 0.0): d = float * 480 - 90
    return d

def DbToFloat(db):
    if (db < -60): f = (db + 90) / 480
    elif (db < -30): f = (db + 70) / 160
    elif (db < -10): f = (db + 50) / 80
    elif (db <= 10): f = (db + 30) / 40
    return int(f * 1023.5) / 1023.0

class OSC:
    def __init__(self, ip, port=10023, host=10024, timeout=5) -> None:
        self.IP = ip
        self.PORT = port
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.SOCK.bind(('127.0.0.1', host))
        self.SOCK.setblocking(0)
        self.HOST = host
        self.TIMEOUT = timeout
        self.QUEUE = queue.Queue()

    def setIP(self, newIP):
        self.IP = newIP

    def send(self, OSCMessage: 'ConstructOSCMessage') -> None:
        print(f'[CLIENT] SENDING MESSAGE: {OSCMessage.MESSAGE} {OSCMessage.VALUE_ARRAY}')
        self.SOCK.sendto(bytes(PadString(OSCMessage.MESSAGE) + PadString(',' + OSCMessage.TYPE_STRING), 'ascii') + OSCMessage.VALUE_ARRAY, (self.IP, self.PORT))

        # serverThread = threading.Thread(target=self.receive, args=(OSCMessage, self.decode))
        # serverThread.start()

        # return self.QUEUE.get()

        # return self.receive(OSCMessage, self.decode)

    def receive(self, msg: 'ConstructOSCMessage', callback):
        ready = select.select([self.SOCK], [], [], 5)
        if ready[0]:
            data, addr = self.SOCK.recvfrom(1024)
            # print(f"[SERVER] RECEIVED MESSAGE: {data} from {addr}")
            try:
                res = callback(data)
                self.QUEUE.put(res)
            except:
                raise Exception(f'There was an error parsing the response from the message {msg.MESSAGE}')
        
    def decode(self, data):
        split = data.split(b',')
        msg = split[0].decode()
        data = split[1]

        data = [data[i:i+1] for i in range(0, len(data), 1)]

        # TODO: there has to be a better way to do this
        types = []
        eots = False
        segments = []
        temp = []
        v = 0
        x = 0
        parsed = ()
        for i, byte in enumerate(data):
            if eots:
                v += 1
                if v < 4:
                    temp.append(byte)
                else:
                    temp.append(byte)
                    segments.append(b''.join(temp))

                    if types[x] == 'f':
                        parsed += (struct.unpack('>f', segments[x])[0], )
                    elif types[x] == 'i':
                        parsed += (struct.unpack('>i', segments[x])[0], )

                    x += 1
                    v = 0
                    temp = []
            try:
                if byte.decode() == 'f' or byte.decode() == 'i' or byte.decode() == 's':
                    types += byte.decode()
            except:
                pass
            
            if byte == b'\0':
                # Add one because counting starts at 0, and another because the comma should be included
                if (i + 2) % 4 == 0:
                    eots = True
                

        return parsed

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
