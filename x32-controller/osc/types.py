import struct

_INT_DGRAM_LEN = 4
_INT64_DGRAM_LEN = 8
_UINT64_DGRAM_LEN = 8
_FLOAT_DGRAM_LEN = 4
_DOUBLE_DGRAM_LEN = 8
_TIMETAG_DGRAM_LEN = 8

_STRING_DGRAM_PAD = 4
_BLOB_DGRAM_PAD = 4
_EMPTY_STR_DGRAM = b'\x00\x00\x00\x00'

def get_string(dgram: bytes, start_index: int):

    offset = 0

    if (len(dgram) > start_index + _STRING_DGRAM_PAD and dgram[start_index + _STRING_DGRAM_PAD] == _EMPTY_STR_DGRAM):
            return '', start_index + _STRING_DGRAM_PAD
    
    while dgram[start_index + offset] != 0:
        offset += 1

    if (offset) % _STRING_DGRAM_PAD == 0:
        offset += _STRING_DGRAM_PAD
    else:
        offset += (-offset % _STRING_DGRAM_PAD)

    data_str = dgram[start_index:start_index + offset]
    return data_str.replace(b'\x00', b'').decode('utf-8'), start_index + offset

def get_int(dgram: bytes, start_index: int):

    return (struct.unpack('>i', dgram[start_index:start_index + _INT_DGRAM_LEN])[0], start_index + _INT_DGRAM_LEN)

def get_float(dgram: bytes, start_index: int):

    return (struct.unpack('>f', dgram[start_index:start_index + _FLOAT_DGRAM_LEN])[0], start_index + _FLOAT_DGRAM_LEN)

def get_blob(dgram: bytes, start_index: int):

    size, int_offset = get_int(dgram, start_index)

    total_size = size + (-size % _BLOB_DGRAM_PAD)

    return dgram[int_offset:int_offset + size], int_offset + total_size

class Colours:
    OFF = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7

class EQTypes:
    LCut = 0
    LShv = 1
    PEQ = 2
    VEQ = 3
    HShv = 4
    HCut = 5