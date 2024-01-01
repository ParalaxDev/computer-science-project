from PyQt6 import QtCore, QtGui, QtWidgets, uic
import osc, core, utils, ui.widgets

QEdit = uic.loadUiType("x32-controller/assets/ui/edit-channel-window.ui")[0]

class EditChannelWindow(QtWidgets.QDialog, QEdit):
    def __init__(self, OSC: osc.controller, SOURCE: core.channel or core.bus or core.matrix, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.OSC = OSC
        self.setWindowTitle(f'Edit {SOURCE.NAME}')
        self.SOURCE = SOURCE

        self.updateMeter(1)

        self._meter = ui.widgets.Meter(["#00ff00", "#00ff00","#00ff00","#00ff00","#00ff00","#00ff00","#00ff00","#00ff00","#fca503","#fca503", "#fca503", "#fca503", "#fca503", "#ff0000", "#ff0000", "#ff0000"], self)
        self._meter.setGeometry(20, 50, 31, 201)
        self._meter.setParent(self.config)

        self._gainDial.valueChanged.connect(self.trimChanged)
        self._lowcutDial.valueChanged.connect(self.lowcutChanged)
        self._delayDial.valueChanged.connect(self.delayChanged)

        self._lowcutToggle.clicked.connect(self.lowcutToggled)
        self._delayToggle.clicked.connect(self.delayToggled)

        self._colourDropdown.currentTextChanged.connect(self.colourChanged)
        self._channelName.textChanged.connect(self.nameChanged)

        self._linkToggle.clicked.connect(self.linkToggled)
        self._phantomToggle.clicked.connect(self.phantomToggled)

        self._gateGraph = ui.widgets.GateGraph()
        self._gateGraph.setGeometry(10, 10, 210, 260)
        self._gateGraph.setParent(self.gate)
        self._gateThreshSlider.valueChanged.connect(self.gateThreshChanged)
        self._gateRangeSlider.valueChanged.connect(self.gateRangeChanged)
        self._gateToggle.clicked.connect(self.gateToggled)

        self._dynGraph = ui.widgets.DynamicsGraph()
        self._dynGraph.setGeometry(10, 10, 210, 260)
        self._dynGraph.setParent(self.dynamics)

        self.redraw()

    def redraw(self):
        print('LOCAL REDRAW')
        self._channelName.setText(self.SOURCE.NAME)
        self._gainDial.setValue(int(self.SOURCE.HEADAMP_GAIN))
        self._lowcutDial.setValue(int(self.SOURCE.HP_FREQ))
        self._delayDial.setValue(int(self.SOURCE.DELAY_TIME))
        self._colourDropdown.setCurrentIndex(self.SOURCE.COLOUR - 1)

        self._delayToggle.setChecked(self.SOURCE.DELAY_ON)
        self._delayToggle.setText('Enabled' if self.SOURCE.DELAY_ON else 'Enable')

        self._lowcutToggle.setChecked(self.SOURCE.HP_ON)
        self._lowcutToggle.setText('Enabled' if self.SOURCE.HP_ON else 'Enable')

        self._linkToggle.setChecked(self.SOURCE.LINK)
        self._phantomToggle.setChecked(self.SOURCE.PHANTOM)

        self._gateToggle.setChecked(self.SOURCE.GATE_ON)
        self._gateToggle.setText('Disable Gate' if self.SOURCE.GATE_ON else 'Enable Gate')
        self._gateThreshLabel.setText(f'{self.SOURCE.GATE_THRESH}hz')
        self._gateRangeLabel.setText(f'{self.SOURCE.GATE_RANGE}db')
        self._gateThreshSlider.setValue(int(self.SOURCE.GATE_THRESH))
        self._gateRangeSlider.setValue(int(self.SOURCE.GATE_RANGE))
        self._gateGraph._trigger_refresh()

        self._dynToggle.setChecked(self.SOURCE.DYN_ON)
        self._dynToggle.setText('Disable Dynamics' if self.SOURCE.DYN_ON else 'Enable Dynamics')
        self._dynThreshLabel.setText(f'{self.SOURCE.DYN_THRESH}hz')
        self._dynRatioLabel.setText(f'{self.SOURCE.DYN_RATIO}db')
        self._dynThreshSlider.setValue(int(self.SOURCE.DYN_THRESH))
        self._dynRatioSlider.setValue(int(self.SOURCE.GATE_RANGE))
        self._dynGraph._trigger_refresh()

    def gateToggled(self, val):
        self.SOURCE.updateGate(val)
        self._gateToggle.setChecked(self.SOURCE.GATE_ON)
        self._gateToggle.setText('Disable Gate' if self.SOURCE.GATE_ON else 'Enable Gate')
        self._gateGraph._trigger_refresh()

    def gateThreshChanged(self, val):
        self.SOURCE.updateGateThresh(float(val))
        self._gateThreshLabel.setText(f'{val}hz')
        self._gateGraph._trigger_refresh()

    def gateRangeChanged(self, val):
        self.SOURCE.updateGateRange(float(val))
        self._gateRangeLabel.setText(f'{val}db')
        self._gateGraph._trigger_refresh()

    def linkToggled(self):
        self.SOURCE.updateLink(not self.SOURCE.LINK)
        self._linkToggle.setChecked(self.SOURCE.LINK)

    def phantomToggled(self):
        self.SOURCE.updatePhantomPowerToggle(not self.SOURCE.PHANTOM)
        self._phantomToggle.setChecked(self.SOURCE.PHANTOM)

    def nameChanged(self, val):
        self.SOURCE.updateName(val)
        self.parent().parent().parent().parent().parent().parent().parent().redraw()

    def colourChanged(self, val):
        self.SOURCE.updateColour(str(val).lower())

    def trimChanged(self, val):
        self.SOURCE.updateHeadampGain(float(val))
        self._gainLevel.setText(f'{"" if val < 0 else "+"}{float(val)}db')

    def lowcutChanged(self, val):
        self.SOURCE.updateHighPassFreq(float(val))
        self._lowcutLevel.setText(f'{val}hz')

    def delayChanged(self, val):
        self.SOURCE.updateDelayTime(val)
        self._delayLevel.setText(f'{float(val)}ms')

    def lowcutToggled(self):
        self.SOURCE.updateHighPassToggle(not self.SOURCE.HP_ON)
        self._lowcutToggle.setChecked(self.SOURCE.HP_ON)
        self._lowcutToggle.setText('Enabled' if self.SOURCE.HP_ON else 'Enable')

    def delayToggled(self):
        self.SOURCE.updateDelay(not self.SOURCE.DELAY_ON)
        self._delayToggle.setChecked(self.SOURCE.DELAY_ON)
        self._delayToggle.setText('Enabled' if self.SOURCE.DELAY_ON else 'Enable')

    def updateMeter(self, val):
        self.meter = val
        self._meterLabel.setText(f'{utils.FloatToDb(val)}db')
        # self._meter._trigger_refresh()
