from utils import TypeToName
from OSC import OSC, ConstructOSCMessage

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

        self.ID = id
        self.TYPE = type

        self.NAME = f'{TypeToName(type)}{id}'
        self.COLOUR = None
        self.SOURCE = id

        self.DELAY = False
        self.DELAY_TIME = 0

        self.GAIN = 0
        self.TRIM = 0

    def populateFields(self):
        one, two, three = self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/config/name', [{'s': self.NAME}]))
        print(one, two, three)



    def triggerError(self, msg):
        print(f'ERROR: {msg}')
        pass

    def updateName(self, val):
        if val > 12 or val < 1:
            self.triggerError('Name should be at least 1 character and no longer than 12 characters')
        else:
            self.NAME = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/config/name', [{'s': self.NAME}]))

    def updateColour(self, col):
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
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/config/color', [{'i': self.COLOUR}]))

    def updateSource(self, val):
        if val > 0 and val < 64:
            self.SOURCE = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/config/source', [{'i': self.SOURCE}]))
        else:
            self.triggerError('Not a valid source')

    def updateDelay(self, val):
        if val == True or val == False:
            self.DELAY = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/delay/on', [{'i': 0 if self.DELAY else 1}]))
        else:
            self.triggerError('Value is not a boolean')

    def updateDelayTime(self, val):
        if val > 0.3 or val < 500:
            self.DELAY_TIME = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/delay/time', [{'f': round(self.DELAY_TIME, 1)}]))
        else:
            self.triggerError('Value is not between 0.3 and 500 ms')

    def updateGain(self, val):
        if val >= 0 and val <= 1:
            self.GAIN = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/mix/fader', [{'f': self.GAIN}]))
        else:
            self.triggerError('Not a valid float between 0 and 1')

    def updateTrim(self, val):
        if val >= 0 and val <= 1:
            self.TRIM = val
            self.OSC.send(ConstructOSCMessage(f'/{self.TYPE}/{str(self.ID+1).zfill(2)}/preamp/trim', [{'f': self.GAIN}]))
        else:
            self.triggerError('Not a valid float between 0 and 1')

class Channel(Base):
    def __init__(self, OSC: 'OSC', id) -> None:
        super().__init__(OSC, id, 'ch')
        pass



osc = OSC('127.0.0.1')
test = Channel(osc, 0)
test.populateFields()