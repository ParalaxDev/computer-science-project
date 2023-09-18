import math

def PadString(msg):	
    str_length = math.ceil((len(msg)+1) / 4.0) * 4
    nulls = '\0' * (str_length - len(msg))
    return msg + nulls