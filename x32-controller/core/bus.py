import core
import osc

class Bus(core.base):
    def __init__(self, OSC: osc.controller, id) -> None:
        super().__init__(OSC, id, 'bus')