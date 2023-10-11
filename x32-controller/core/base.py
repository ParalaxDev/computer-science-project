import osc
import utils.log
import osc.types

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

        self.GATE_ON, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/on'))
        self.GATE_THRESH, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/thr'))
        self.GATE_RANGE, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/range'))

        self.DYN_ON, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/on'))
        self.DYN_THRESH, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/thr'))

        self.EQ_ON, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/on'))

        self.EQ_1_TYPE, = (None, )
        self.EQ_1_F, = (None, )
        self.EQ_1_G, = (None, )
        self.EQ_1_Q, = (None, )

        self.EQ_2_TYPE, = (None, )
        self.EQ_2_F, = (None, )
        self.EQ_2_G, = (None, )
        self.EQ_2_Q, = (None, )

        self.EQ_3_TYPE, = (None, )
        self.EQ_3_F, = (None, )
        self.EQ_3_G, = (None, )
        self.EQ_3_Q, = (None, )

        self.EQ_4_TYPE, = (None, )
        self.EQ_4_F, = (None, )
        self.EQ_4_G, = (None, )
        self.EQ_4_Q, = (None, )

        self.GAIN, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader'))
        self.MUTE, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on'))
        self.PAN = (None, )


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

    def updateGate(self, val:bool) -> None:
        if type(val) == bool:
            self.GATE_ON = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/on', [{'i': 0 if self.GATE_ON else 1}]))
        else:
            self.triggerError('Gate value is not a boolean')

    def updateGateThresh(self, val: float) -> None:
        if type(val) == float and val > -80 or val < 0:
            self.GATE_THRESH = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/thr', [{'f': round(self.GATE_THRESH, 1)}]))
        else:
            self.triggerError('Gate threshold value is not between -80 and 0 db')

    def updateGateRange(self, val: float) -> None:
        if type(val) == float and val > 3 or val < 60:
            self.GATE_RANGE = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/range', [{'f': round(self.GATE_RANGE, 1)}]))
        else:
            self.triggerError('Gate range value is not between 3 and 60 db')

    def updateDynamics(self, val: bool) -> None:
        if type(val) == bool:
            self.DYN_ON = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/on', [{'i': 0 if self.DYN_ON else 1}]))
        else:
            self.triggerError('Dynamics value is not a boolean')

    def updateDynamicsThresh(self, val: float) -> None:
        if type(val) == float and val > -60 or val < 0:
            self.DYN_THRESH = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/thr', [{'f': round(self.DYN_THRESH, 1)}]))
        else:
            self.triggerError('Dynamics threshold value is not between -60 and 0 db')

    def updateEq(self, val: bool) -> None:
        if type(val) == bool:
            self.EQ_ON = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/on', [{'i': 0 if self.EQ_ON else 1}]))
        else:
            self.triggerError('EQ value is not a boolean')

    def updateEq1Type(self, val: osc.types.EQTypes) -> None:
        pass

    def updateEq1Freq(self, val: float) -> None:
        if type(val) == float and val > 20 or val < 20000:
            self.EQ_1_F = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/f', [{'f': round(self.EQ_1_F, 1)}]))
        else:
            self.triggerError('EQ frequency value is not between 20 and 20000 hz')

    def updateEq1Gain(self, val: float) -> None:
        if type(val) == float and val > -15 or val < 15:
            self.EQ_1_G = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/g', [{'f': round(self.EQ_1_G, 1)}]))
        else:
            self.triggerError('EQ gain value is not between -15 and 15 db')

    def updateEq1Q(self, val: float) -> None:
        if type(val) == float and val > 0.3 or val < 10:
            self.EQ_1_Q = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/q', [{'f': round(self.EQ_1_Q, 1)}]))
        else:
            self.triggerError('EQ Q value is not between 0.3 and 10')

    def updatePan(self, val: float) -> None:
        if type(val) == float and val > -100 or val < 100:
            self.PAN = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/pan', [{'f': round(self.PAN, 1)}]))
        else:
            self.triggerError('Pan value is not between -100 and 100')
