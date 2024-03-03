import osc
import database
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
        self.UID = self.TYPE + '-' + str(self.ID)

        self.NAME = "None"
        self.COLOUR = 0
        self.SOURCE = 0

        self.DELAY_ON = 0
        self.DELAY_TIME = 0

        self.GATE_ON = 0
        self.GATE_THRESH = 0
        self.GATE_RANGE = 0

        self.DYN_ON = 0
        self.DYN_THRESH = 0
        self.DYN_RATIO = 0  # TODO: Implement this

        self.EQ_ON = 0

        self.EQ_1_TYPE = 0
        self.EQ_1_F = 0
        self.EQ_1_G = 0
        self.EQ_1_Q = 0

        self.EQ_2_TYPE = 0
        self.EQ_2_F = 0
        self.EQ_2_G = 0
        self.EQ_2_Q = 0

        self.EQ_3_TYPE = 0
        self.EQ_3_F = 0
        self.EQ_3_G = 0
        self.EQ_3_Q = 0

        self.EQ_4_TYPE = 0
        self.EQ_4_F = 0
        self.EQ_4_G = 0
        self.EQ_4_Q = 0

        self.GAIN = 0
        self.MUTE = 0
        self.PAN = 0

    def __str__(self) -> str:
        return f'FADER {self.NAME} is at {self.GAIN} from {self.SOURCE}'

    def loadValues(self) -> None:
        res, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/name'))
        self.NAME = f'Channel {self.ID}' if res == 0 else res
        self.COLOUR, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/color'))
        self.SOURCE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/source'))


        self.DELAY_ON, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/on'))
        self.DELAY_TIME, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/time'))

        self.GATE_ON, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/on'))
        self.GATE_THRESH, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/thr'))
        self.GATE_RANGE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/range'))

        self.DYN_ON, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/on'))
        self.DYN_THRESH, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/thr'))
        self.DYN_RATIO, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/thr'))  # TODO: Implement this

        self.EQ_ON, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/on'))

        self.EQ_1_TYPE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/type'))
        self.EQ_1_F, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/f'))
        self.EQ_1_G, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/g'))
        self.EQ_1_Q, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/q'))

        self.EQ_2_TYPE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/2/type'))
        self.EQ_2_F, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/2/f'))
        self.EQ_2_G, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/2/g'))
        self.EQ_2_Q, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/2/q'))

        self.EQ_3_TYPE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/3/type'))
        self.EQ_3_F, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/3/f'))
        self.EQ_3_G, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/3/g'))
        self.EQ_3_Q, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/3/q'))

        self.EQ_4_TYPE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/4/type'))
        self.EQ_4_F, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/4/f'))
        self.EQ_4_G, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/4/g'))
        self.EQ_4_Q, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/4/q'))

        self.GAIN, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader'))
        self.MUTE, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on'))
        self.PAN, = self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/pan'))

    def saveValuesToDb(self, db: database.controller):
        db.execute(f'''
            INSERT INTO bases (
                name,
                colour,
                source,
                delay_on, delay_time,
                gate_on, gate_thresh, gate_range,
                dyn_on, dyn_thresh, dyn_ratio,
                eq_on,
                eq_1_type, eq_1_f, eq_1_g, eq_1_q,
                eq_2_type, eq_2_f, eq_2_g, eq_2_q,
                eq_3_type, eq_3_f, eq_3_g, eq_3_q,
                eq_4_type, eq_4_f, eq_4_g, eq_4_q,
                gain,
                mute,
                pan
            ) VALUES (
                "{self.NAME}",
                "{self.COLOUR}",
                "{self.SOURCE}",
                "{self.DELAY_ON}", "{self.DELAY_TIME}",
                "{self.GATE_ON}", "{self.GATE_THRESH}", "{self.GATE_RANGE}",
                "{self.DYN_ON}", "{self.DYN_THRESH}", "{self.DYN_RATIO}",
                "{self.EQ_ON}",
                "{self.EQ_1_TYPE}", "{self.EQ_1_F}", "{self.EQ_1_G}", "{self.EQ_1_Q}",
                "{self.EQ_2_TYPE}", "{self.EQ_2_F}", "{self.EQ_2_G}", "{self.EQ_2_Q}",
                "{self.EQ_3_TYPE}", "{self.EQ_3_F}", "{self.EQ_3_G}", "{self.EQ_3_Q}",
                "{self.EQ_4_TYPE}", "{self.EQ_4_F}", "{self.EQ_4_G}", "{self.EQ_4_Q}",
                "{self.GAIN}",
                "{self.MUTE}",
                "{self.PAN}"
            )
        ''')

        return db.cursor.lastrowid

    def updateValuesInDb(self, db: database.controller, baseId: int):
        db.execute(f'''
            UPDATE bases SET
            name = "{self.NAME}",
            colour = "{self.COLOUR}",
            source = "{self.SOURCE}",
            link = "{self.LINK}",
            delay_on = "{self.DELAY_ON}",
            delay_time = "{self.DELAY_TIME}",
            gate_on = "{self.GATE_ON}",
            gate_thresh = "{self.GATE_THRESH}",
            gate_range = "{self.GATE_RANGE}",
            dyn_on = "{self.DYN_ON}",
            dyn_thresh = "{self.DYN_THRESH}",
            dyn_ratio = "{self.DYN_RATIO}",
            eq_on = "{self.EQ_ON}",
            eq_1_type = "{self.EQ_1_TYPE}",
            eq_1_f = "{self.EQ_1_F}",
            eq_1_g = "{self.EQ_1_G}",
            eq_1_q = "{self.EQ_1_Q}",
            gain = "{self.GAIN}",
            mute = "{self.MUTE}",
            pan = "{self.PAN}"
            WHERE id = "{baseId}"
        ''')

    def loadValuesFromDb(self, db: database.controller, baseId: int):
        vals = db.execute(f'SELECT * FROM bases WHERE id = {baseId}')

        if not vals:
            self.triggerError('Error loading data from db')
        else:
            id, name, colour, source, link, delayOn, delayTime, gateOn, gateThresh, gateRange, dynOn, dynThresh, dynRatio, eqOn, eq1Type, eq1F, eq1G, eq1Q, eq2Type, eq2F, eq2G, eq2Q, eq3Type, eq3F, eq3G, eq3Q, eq4Type, eq4F, eq4G, eq4Q, gain, mute, pan = vals.fetchone()

            self.updateName(name)
            self.updateColour(colour)
            self.updateSource(source)
            self.updateLink(link)
            self.updateDelay(delayOn)
            self.updateDelayTime(delayTime)
            self.updateGate(gateOn)
            self.updateGateThresh(gateThresh)
            self.updateGateRange(gateRange)
            self.updateDynamics(dynOn)
            self.updateDynamicsThresh(dynThresh)
            self.updateDynamicsRatio(dynRatio)
            self.updateEq(eqOn)
            self.updateGain(gain)
            self.updateMute(mute)

    def triggerError(self, msg: str) -> None:
        utils.log.error(msg)

    def updateName(self, val: str) -> None:
        if type(val) == str and len(val) > 12 or len(val) < 1:
            self.triggerError(
                'Name should be at least 1 character and no longer than 12 characters')
        else:
            self.NAME = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/name', [{'s': self.NAME}]))

    def updateColour(self, col: str or int):
        colcode = None

        if isinstance(col, str):
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
                colcode = osc.colours.GREEN
        else:
            colcode = col

        self.COLOUR = colcode
        self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/color', [{'i': self.COLOUR}]))

    def updateSource(self, val: int) -> None:
        if type(val) == int and val >= 0 and val < 64:
            self.SOURCE = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/config/source', [{'i': self.SOURCE}]))
        else:
            self.triggerError('Not a valid source')

    def updateLink(self, val: bool) -> None:
        val = bool(val)
        self.LINK = val
        self.OSC.send(osc.construct(
            f'/config/{self.TYPE}link/{f"{self.ID - 1}-{self.ID}" if self.ID % 2 == 0 else f"{self.ID}-{self.ID + 1}"}', [{'i': 1 if self.LINK else 0}]))

    def updateDelay(self, val: bool) -> None:
        val = bool(val)
        self.DELAY_ON = val
        self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/on', [{'i': 1 if self.DELAY_ON else 0}]))

    def updateDelayTime(self, val: float) -> None:
        if type(val) == float and val > 0.3 or val < 500:
            self.DELAY_TIME = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/delay/time', [{'f': round(self.DELAY_TIME, 1)}]))
        else:
            self.triggerError('Delay time value is not between 0.3 and 500 ms')

    def updateGain(self, val: float) -> None:
        if type(val) == float and val >= 0 and val <= 1:
            self.GAIN = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/fader', [{'f': self.GAIN}]))
        else:
            self.triggerError('Gain is not a valid float between 0 and 1')

    def updateMute(self, val: bool) -> None:
        val = bool(val)
        self.MUTE = val
        self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/on', [{'i': 1 if self.MUTE else 0}]))

    def updateGate(self, val: bool) -> None:
        val = bool(val)
        self.GATE_ON = val
        self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/on', [{'i': 1 if self.GATE_ON else 0}]))

    def updateGateThresh(self, val: float) -> None:
        if type(val) == float and val > -80 or val < 0:
            self.GATE_THRESH = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/thr', [{'f': round(self.GATE_THRESH, 1)}]))
        else:
            self.triggerError(
                'Gate threshold value is not between -80 and 0 db')

    def updateGateRange(self, val: float) -> None:
        if type(val) == float and val > 3 or val < 60:
            self.GATE_RANGE = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/range', [{'f': round(self.GATE_RANGE, 1)}]))
        else:
            self.triggerError('Gate range value is not between 3 and 60 db')

    def updateDynamics(self, val: bool) -> None:
        val = bool(val)
        self.DYN_ON = val
        self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/on', [{'i': 1 if self.DYN_ON else 0}]))

    def updateDynamicsThresh(self, val: float) -> None:
        if type(val) == float and val > -60 or val < 0:
            self.DYN_THRESH = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/thr', [{'f': round(self.DYN_THRESH, 1)}]))
        else:
            self.triggerError(
                'Dynamics threshold value is not between -60 and 0 db')

    def updateDynamicsRatio(self, val):
        if type(val) == int and val > 0 or val < 11:
            self.DYN_RATIO = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/dyn/ratio', [{'i': self.DYN_RATIO}]))
        else:
            self.triggerError(
                'Dynamics ratio value is not between 0 and 11')

    def updateEq(self, val: bool) -> None:
        val = bool(val)
        self.EQ_ON = val
        self.OSC.send(osc.construct(
            f'/{self.TYPE}/{str(self.ID).zfill(2)}/gate/on', [{'i': 1 if self.EQ_ON else 0}]))

    def updateEq1Type(self, val: osc.types.EQTypes) -> None:
        pass

    def updateEq1Freq(self, val: float) -> None:
        if type(val) == float and val > 20 or val < 20000:
            self.EQ_1_F = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/f', [{'f': round(self.EQ_1_F, 1)}]))
        else:
            self.triggerError(
                'EQ frequency value is not between 20 and 20000 hz')

    def updateEq1Gain(self, val: float) -> None:
        if type(val) == float and val > -15 or val < 15:
            self.EQ_1_G = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/g', [{'f': round(self.EQ_1_G, 1)}]))
        else:
            self.triggerError('EQ gain value is not between -15 and 15 db')

    def updateEq1Q(self, val: float) -> None:
        if type(val) == float and val > 0.3 or val < 10:
            self.EQ_1_Q = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/eq/1/q', [{'f': round(self.EQ_1_Q, 1)}]))
        else:
            self.triggerError('EQ Q value is not between 0.3 and 10')

    def updatePan(self, val: float) -> None:
        if type(val) == float and val > -100 or val < 100:
            self.PAN = val
            self.OSC.send(osc.construct(
                f'/{self.TYPE}/{str(self.ID).zfill(2)}/mix/pan', [{'f': round(self.PAN, 1)}]))
        else:
            self.triggerError('Pan value is not between -100 and 100')
