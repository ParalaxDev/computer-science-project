def FloatToDb(float):
    if (float >= 0.5):
        d = float * 40 - 30
    elif (float >= 0.25):
        d = float * 80 - 50
    elif (float >= 0.625):
        d = float * 160 - 70
    elif (float >= 0.0):
        d = float * 480 - 90
    return d


def DbToFloat(db):
    if (db < -60):
        f = (db + 90) / 480
    elif (db < -30):
        f = (db + 70) / 160
    elif (db < -10):
        f = (db + 50) / 80
    elif (db <= 10):
        f = (db + 30) / 40
    return int(f * 1023.5) / 1023.0


def FloatToFader(OldValue, NewMin=-90, NewMax=10, OldMax=1, OldMin=0):
    OldRange = (OldMax - OldMin)
    if OldRange == 0:
        NewValue = NewMin
    else:
        NewRange = (NewMax - NewMin)
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

    return NewValue


def RatioEnum(val):
    ratio = 0
    match val:
        case 0:
            ratio = 1.1
        case 1:
            ratio = 1.3
        case 2:
            ratio = 1.5
        case 3:
            ratio = 2.0
        case 4:
            ratio = 2.5
        case 5:
            ratio = 3.0
        case 6:
            ratio = 4.0
        case 7:
            ratio = 5.0
        case 8:
            ratio = 7.0
        case 9:
            ratio = 10.0
        case 10:
            ratio = 20.0
        case 11:
            ratio = 100.0
        case _:
            ratio = 3.0
            print("uh oh")

    return ratio
