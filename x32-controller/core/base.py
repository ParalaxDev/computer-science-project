import osc
import utils.log

class Base:
    def __init__(self, OSC: osc.controller, id, type) -> None:
        self.OSC = OSC

        if id <= 0 or id > 32:
            utils.log.error(f'{id} is not a valid number for fader')
            raise Exception()
        
        self.ID = id
        self.TYPE = type
        self.UUID = self.TYPE + str(self.ID)

        self.loadValues()

    def __str__(self) -> str:
        return f'FADER {self.NAME} is at {self.GAIN} from {self.SOURCE}'

    def loadValues(self) -> None:
        self.NAME, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/name'))
        self.COLOUR, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/color'))
        self.SOURCE, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/source'))
        self.LINK, = self.OSC.send(osc.construct(f'/config/{self.TYPE}link/{f"{self.ID - 1}-{self.ID}" if self.ID % 2 == 0 else f"{self.ID}-{self.ID + 1}"}'))

        self.DELAY_ON, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/on'))
        self.DELAY_TIME, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/time'))

        self.GAIN, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader'))

        self.MUTE, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on'))

    def triggerError(self, msg: str) -> None:
        utils.log.error(msg)

    def updateName(self, val: str) -> None:
        if type(val) == str and len(val) > 12 or len(val) < 1:
            self.triggerError('Name should be at least 1 character and no longer than 12 characters')
        else:
            self.NAME = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/name', [{'s': self.NAME}]))

    def updateColour(self, col: str):
        colcode = None
        col = col.lower()
        if col == 'red':
            colcode = osc.colours.RED
        elif col == 'green':
            colcode = osc.colours.GREEN
        elif col == 'yellow':
            colcode = osc.colours.YELLOW
        elif col == 'blue':
            colcode = osc.colours.BLUE
        elif col == 'magenta':
            colcode = osc.colours.MAGENTA
        elif col == 'cyan':
            colcode = osc.colours.CYAN
        elif col == 'white':
            colcode = osc.colours.WHITE

        if colcode == None:
            self.triggerError('Not a valid colour')
        else:
            self.COLOUR = colcode
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/color', [{'i': self.COLOUR}]))

    def updateSource(self, val: int) -> None:
        if type(val) == int and val > 0 and val < 64:
            self.SOURCE = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/source', [{'i': self.SOURCE}]))
        else:
            self.triggerError('Not a valid source')

    def updateLink(self, val: bool) -> None:
        if type(val) == bool:
            self.LINK = val
            self.OSC.send(osc.construct(f'/config/{self.TYPE}link/{f"{self.ID - 1}-{self.ID}" if self.ID % 2 == 0 else f"{self.ID}-{self.ID + 1}"}', [{'i': 0 if self.LINK else 1}]))
        else:
            self.triggerError('Link toggle is not a boolean')

    def updateDelay(self, val: bool) -> None:
        if type(val) == bool:
            self.DELAY_ON = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/on', [{'i': 0 if self.DELAY_ON else 1}]))
        else:
            self.triggerError('Delay toggle is not a boolean')

    def updateDelayTime(self, val: float) -> None:
        if type(val) == float and val > 0.3 or val < 500:
            self.DELAY_TIME = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/time', [{'f': round(self.DELAY_TIME, 1)}]))
        else:
            self.triggerError('Delay time value is not between 0.3 and 500 ms')

    def updateGain(self, val: float) -> None:
        if type(val) == float and val >= 0 and val <= 1:
            self.GAIN = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader', [{'f': self.GAIN}]))
        else:
            self.triggerError('Gain is not a valid float between 0 and 1')

    def updateMute(self, val: bool) -> None:
        if type(val) == bool:
            self.MUTE = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on', [{'i': 0 if self.MUTE else 1}]))
        else:
            self.triggerError('Mute value is not a boolean')