import osc
import utils.log
from osc import types
import time

utils.log.setLogging(True)


test = osc.controller('192.168.0.2', live=True, localIP="192.168.0.2")


def log():
    print(test.METER_DATA)


test.setMeterCallback(log)

# while True:
res1 = test.send(osc.construct("/info"))
# res2 = test.send(osc.construct("/ch/02/mix/fader"))
# res3 = test.send(osc.construct("/ch/03/mix/fader"))
utils.log.error(res1)
# utils.log.error(res2)
# utils.log.error(res3)
time.sleep(.5)
