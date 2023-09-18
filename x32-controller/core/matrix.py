import core
import osc

class Matrix(core.base):
    def __init__(self, OSC: osc.controller, id) -> None:
        super().__init__(OSC, id, 'mtx')