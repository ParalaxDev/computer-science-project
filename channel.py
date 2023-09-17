from utils import TypeToName
from OSC import OSC, ConstructOSCMessage
import log

class Colours:
    OFF = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7

class Base:
    def __init__(self, OSC: 'OSC', id, type) -> None:
        self.OSC = OSC

        if id <= 0 or id > 32:
            log.error(f'{id} is not a valid number for fader')
            raise Exception()
        
        self.ID = id
        self.TYPE = type
        self.UUID = self.TYPE + str(self.ID)

        self.NAME = ''
        self.COLOUR = Colours.OFF
        self.SOURCE = 0
        self.LINK = False

        self.HEADAMP_SOURCE = 0
        self.HEADAMP_GAIN = 0

        self.DELAY_ON = False
        self.DELAY_TIME = 0

        self.GAIN = 0
        

        self.MUTE = False 

    def __str__(self) -> str:
        return f'FADER {self.NAME} is at {self.GAIN} from {self.SOURCE}'

    def populateFields(self):
        self.NAME, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/name'))
        self.COLOUR, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/color'))
        self.SOURCE, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/source'))
        self.LINK, = self.OSC.send(ConstructOSCMessage(f'/config/{self.TYPE}link/{f"{self.ID - 1}-{self.ID}" if self.ID % 2 == 0 else f"{self.ID}-{self.ID + 1}"}'))

        self.DELAY_ON, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/on'))
        self.DELAY_TIME, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/time'))

        self.GAIN, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader'))

        self.MUTE, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on'))

    def triggerError(self, msg: str) -> None:
        log.error({msg})

    def updateName(self, val: str) -> None:
        if type(val) == str and len(val) > 12 or len(val) < 1:
            self.triggerError('Name should be at least 1 character and no longer than 12 characters')
        else:
            self.NAME = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/name', [{'s': self.NAME}]))

    def updateColour(self, col: str):
        colcode = None
        col = col.lower()
        if col == 'red':
            colcode = Colours.RED
        elif col == 'green':
            colcode = Colours.GREEN
        elif col == 'yellow':
            colcode = Colours.YELLOW
        elif col == 'blue':
            colcode = Colours.BLUE
        elif col == 'magenta':
            colcode = Colours.MAGENTA
        elif col == 'cyan':
            colcode = Colours.CYAN
        elif col == 'white':
            colcode = Colours.WHITE

        if colcode == None:
            self.triggerError('Not a valid colour')
        else:
            self.COLOUR = colcode
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/color', [{'i': self.COLOUR}]))

    def updateSource(self, val: int) -> None:
        if type(val) == int and val > 0 and val < 64:
            self.SOURCE = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/source', [{'i': self.SOURCE}]))
        else:
            self.triggerError('Not a valid source')

    def updateLink(self, val: bool) -> None:
        if type(val) == bool:
            self.LINK = val
            self.OSC.send(ConstructOSCMessage(f'/config/{self.TYPE}link/{f"{self.ID - 1}-{self.ID}" if self.ID % 2 == 0 else f"{self.ID}-{self.ID + 1}"}', [{'i': 0 if self.LINK else 1}]))
        else:
            self.triggerError('Link toggle is not a boolean')

    def updateDelay(self, val: bool) -> None:
        if type(val) == bool:
            self.DELAY_ON = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/on', [{'i': 0 if self.DELAY_ON else 1}]))
        else:
            self.triggerError('Delay toggle is not a boolean')

    def updateDelayTime(self, val: float) -> None:
        if type(val) == float and val > 0.3 or val < 500:
            self.DELAY_TIME = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/time', [{'f': round(self.DELAY_TIME, 1)}]))
        else:
            self.triggerError('Delay time value is not between 0.3 and 500 ms')

    def updateGain(self, val: float) -> None:
        if type(val) == float and val >= 0 and val <= 1:
            self.GAIN = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader', [{'f': self.GAIN}]))
        else:
            self.triggerError('Gain is not a valid float between 0 and 1')

    def updateMute(self, val: bool) -> None:
        if type(val) == bool:
            self.MUTE = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on', [{'i': 0 if self.MUTE else 1}]))
        else:
            self.triggerError('Mute value is not a boolean')


class Channel(Base):
    def __init__(self, OSC: 'OSC', id) -> None:
        super().__init__(OSC, id, 'ch')

        self.HEADAMP_SOURCE = 0
        self.HEADAMP_GAIN = 0

        self.HP_ON = False
        self.HP_FREQ = 0

        self.populateFields()

    def populateFields(self):
        self.HEADAMP_SOURCE, = self.OSC.send(ConstructOSCMessage(f'/-ha/{str(self.ID - 1).zfill(2)}/index'))
        self.HEADAMP_GAIN, = self.OSC.send(ConstructOSCMessage(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/gain'))

        print(self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpon')))
        self.HP_FREQ, = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpf'))

        super().populateFields()

    def updateHeadampGain(self, val: float) -> None:
        if type(val) == float and val >= -12 and val <= 60:
            self.HEADAMP_GAIN = val
            self.OSC.send(ConstructOSCMessage(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/gain', [{'f': self.HEADAMP_GAIN}]))
        else:
            self.triggerError('Headamp Gain is not a valid float between -12 and 60')

    def updateHighPassToggle(self, val: bool) -> None:
        if type(val) == bool:
            self.HP_ON = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpon', [{'i': 0 if self.HP_ON else 1}]))
        else:
            self.triggerError('Highpass toggle is not a boolean')

    def updateHighPassFreq(self, val: float) -> None:
        if type(val) == float and val >= 20 and val <= 400:
            self.HP_FREQ = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpf', [{'f': self.HP_FREQ}]))
        else:
            self.triggerError('Highpass frequency is not a valid float between 20 and 400')


class Bus(Base):
    def __init__(self, OSC: OSC, id):
        super().__init__(OSC, id, 'bus')

class Matrix(Base):
    def __init__(self, OSC: OSC, id):
        super().__init__(OSC, id, 'mtx')