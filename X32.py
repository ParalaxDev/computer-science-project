import socket, struct, math, random

UDP_IP = "127.0.0.1"
UDP_PORT = 10023

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def PadString(msg):	
    str_length = math.ceil((len(msg)+1) / 4.0) * 4
    nulls = '\0' * (str_length - len(msg))
    return msg + nulls

class ConstructOSCMessage:
    def __init__(self, message, args) -> None:
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


print('listening...')
while True:
    data, addr = sock.recvfrom(1024)
    print("received data: %s" % data)
    test = ConstructOSCMessage('/ch/01/mix/fader', [{'f': random.uniform(0, 1)}])
    sock.sendto(bytes(PadString(test.MESSAGE) + PadString(',' + test.TYPE_STRING), 'ascii') + test.VALUE_ARRAY, (UDP_IP, 10024))