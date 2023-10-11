import sqlite3
import core
import osc, database

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

    def saveValuesToDb(self, db, saveId, channelId):
        baseId = super().saveValuesToDb(db)

        db.execute(f'''
            INSERT INTO channels (
                save_id,
                base_id,
                channel_num,
                headamp_source, headamp_gain,
                hp_on, hp_freq,
                phantom
            ) VALUES (
                "{saveId}",
                "{baseId}",
                "{channelId}",
                "{self.HEADAMP_SOURCE}", "{self.HEADAMP_GAIN}",
                "{self.HP_ON}", "{self.HP_FREQ}",
                "{self.PHANTOM}"
            )
        ''')

    def loadValuesFromDb(self, db: database.controller, saveId: int, channelId: int):
        vals = db.execute(f'SELECT base_id, headamp_gain, hp_on, hp_freq, phantom from channels WHERE save_id = {saveId} AND channel_num = {channelId}')



        if isinstance(vals, sqlite3.Cursor):
            baseId, headampGain, hpOn, hpFreq, phantom = vals.fetchone()

            self.updateHeadampGain(headampGain)
            self.updateHighPassToggle(hpOn)
            self.updateHighPassFreq(hpFreq)
            self.updatePhantomPowerToggle(phantom)

            super().loadValuesFromDb(db, baseId)

    def updateHeadampGain(self, val: float) -> None:
        val = float(val)
        if val >= -12 and val <= 60:
            self.HEADAMP_GAIN = val
            self.OSC.send(osc.construct(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/gain', [{'f': self.HEADAMP_GAIN}]))
        else:
            self.triggerError('Headamp Gain is not a valid float between -12 and 60')

    def updateHighPassToggle(self, val: bool) -> None:
        val = bool(val)
        self.HP_ON = val
        self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpon', [{'i': 0 if self.HP_ON else 1}]))

    def updateHighPassFreq(self, val: float) -> None:
        val = float(val)
        # TODO: this value should be 20? not sure why its not working rn
        if val >= 0 and val <= 400:
            self.HP_FREQ = val
            self.OSC.send(osc.construct(f'/{self.TYPE}/{str(self.ID).zfill(2)}/preamp/hpf', [{'f': self.HP_FREQ}]))
        else:
            self.triggerError('Highpass frequency is not a valid float between 20 and 400')

    def updatePhantomPowerToggle(self, val: bool) -> None:
        val = bool(val)
        self.PHANTOM = val
        self.OSC.send(osc.construct(f'/headamp/{str(self.HEADAMP_SOURCE).zfill(3)}/phantom', [{'i': 0 if self.PHANTOM else 1}]))
