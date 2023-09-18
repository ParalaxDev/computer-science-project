import core
import osc

class Channel(core.base):
    def __init__(self, OSC: osc.controller, id) -> None:
        super().__init__(OSC, id, 'ch')

        self.loadValues()

    def loadValues(self):

        super().loadValues()

        self.HEADAMP_SOURCE, = self.OSC.send(osc.construct(f'/-ha/{str(self.ID - 1).zfill(2)}/index'))
        self.HEADAMP_GAIN, = self.OSC.send(osc.construct(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/gain'))

        self.HP_ON, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpon'))
        self.HP_FREQ, = self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpf'))

        self.PHANTOM, = self.OSC.send(osc.construct(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/phantom'))

    def updateHeadampGain(self, val: float) -> None:
        if type(val) == float and val >= -12 and val <= 60:
            self.HEADAMP_GAIN = val
            self.OSC.send(osc.construct(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/gain', [{'f': self.HEADAMP_GAIN}]))
        else:
            self.triggerError('Headamp Gain is not a valid float between -12 and 60')

    def updateHighPassToggle(self, val: bool) -> None:
        if type(val) == bool:
            self.HP_ON = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpon', [{'i': 0 if self.HP_ON else 1}]))
        else:
            self.triggerError('Highpass toggle is not a boolean')

    def updateHighPassFreq(self, val: float) -> None:
        if type(val) == float and val >= 20 and val <= 400:
            self.HP_FREQ = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpf', [{'f': self.HP_FREQ}]))
        else:
            self.triggerError('Highpass frequency is not a valid float between 20 and 400')

    def updatePhantomPowerToggle(self, val: bool) -> None:
        if type(val) == bool:
            self.PHANTOM = val
            self.OSC.send(osc.construct(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/phantom', [{'i': 0 if self.PHANTOM else 1}]))
        else:
            self.triggerError('Phantom power toggle is not a boolean')
