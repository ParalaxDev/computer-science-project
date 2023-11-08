import struct
import utils

class Construct:
    def __init__(self, message, args = []) -> None:
        self.MESSAGE = message
        self.TYPE_STRING = ''
        self.VALUE_ARRAY = bytearray()
        for arg in args:
            ty = list(arg.keys())[0]
            self.TYPE_STRING += ty
            val = arg.get(ty)
            try:
                match ty:
                    case 'f':
                        self.VALUE_ARRAY += bytearray(struct.pack(">f", val))
                    case 'i':
                        self.VALUE_ARRAY += bytearray(struct.pack(">i", val))
                    case 's':
                        self.VALUE_ARRAY += bytes(utils.pad(val), 'ascii')
            except Exception as e:
                utils.log.error(f"An error occured generating OSC message: {e}")
