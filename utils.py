import math

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

def TypeToName(type):
    if type == 'ch':
        return 'Channel'
    elif type == 'bus':
        return 'Bus'
    elif type == 'mtx':
        return 'Matrix'
    
def PadString(msg):	
    str_length = math.ceil((len(msg)+1) / 4.0) * 4
    nulls = '\0' * (str_length - len(msg))
    return msg + nulls

class Colours:
    OFF = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7