import socket
import select
import queue
import osc
# import ui
import utils
from osc import types
import time
import threading
import random


class Controller:
    def __init__(self, ip, live=True, port=10023, host=10024, timeout=5, localIP="192.168.0.2") -> None:
        self.IP = ip
        self.PORT = port
        self.LIVE = live
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.METER_DATA = []
        self.EXPECTED_MESSAGES = []
        self.RESULTS = []
        # LOCAL IP BELOW:
        # self.LOCAL_IP = "169.254.70.162"
        self.LOCAL_IP = localIP
        self.SOCK.bind((self.IP, host))
        self.HOST = host
        self.TIMEOUT = timeout
        self.METER_CALLBACK = None
        self.METER_DATA = [0] * 70

        pingThread = threading.Thread(target=self.pingThread)
        collectionThread = threading.Thread(target=self.collectionThread)

        pingThread.start()
        collectionThread.start()

    def setMeterCallback(self, callback):
        self.METER_CALLBACK = callback

    def collectionThread(self):
        utils.log.info(f"STARTING COLLECTION")
        lastUpdate = time.time()

        while True:
            data, addr = self.SOCK.recvfrom(1024)

            m, _ = [e for e in data.split(b',', 1) if e]

            m = m.strip(b'\x00').decode('ascii')

            parsed = list(filter(None, m.split('/')))

            match parsed[0]:
                case "meters":
                    if time.time() - lastUpdate > 0.05:
                        self.METER_DATA = self.decodeMeterBlob(data)
                        if self.METER_CALLBACK:
                            self.METER_CALLBACK()

                    lastUpdate = time.time()
                case "/xremote":
                    self.RESULTS.append({
                        "msg": m,
                        "value": 0
                    })
                    # self.METER_DATA = self.decodeMeterBlob(data)
                case _:
                    try:
                        pos = self.EXPECTED_MESSAGES.index(m)
                        if pos >= 0:
                            utils.log.info(f"FOUND EXPECTED MESSAGE: {m}")
                            self.EXPECTED_MESSAGES.pop(pos)
                            self.RESULTS.append({
                                "msg": m,
                                "value": self.decode(data)
                            })
                    except:
                        utils.log.info(
                            f"RECIEVED UNEXPECTED MESSAGE: {m}")

    def pingThread(self):
        self.OLD_TIME = 0

        while True:
            if time.time() - self.OLD_TIME > 9:
                utils.log.warn(f"RENEWED LEASE ON XREMOTE & METERS")

                # BYPASS BBELOW:
                # self.send(osc.construct("/xremote"))
                self.send(osc.construct("/meters", [{'s': '/meters/0'}]))

                self.OLD_TIME = time.time()

    def decodeMeterBlob(self, data: bytes):
        # data, = self.decode(data)
        # count, index = types.get_int_small(data, 0)
        # data = data[index:]

        pos = 0
        res = []
        # try:
        #     for _ in range(count):
        #         x, pos = types.get_float_small(data, pos)
        #         res.append(x)
        # except:
        for _ in range(70):
            x = random.random()
            res.append(x)

        return res
        # utils.log.error(f"ERROR PARSING METER DATA")

    def setIP(self, newIP):
        self.IP = newIP

    def setPort(self, newPort):
        self.PORT = newPort

    def setLive(self, newLive):
        self.LIVE = newLive

    def searchResults(self, array, key, value):
        for obj in array:
            if key in obj and obj[key] == value:
                return obj
        return None

    def checkMessages(self, arr, val):
        for dictionary in arr:
            if dictionary.get("msg") == val:
                return True
        return False

    def send(self, OSCMessage: osc.construct) -> tuple or None:

        if self.LIVE:
            if OSCMessage.MESSAGE[0] != '/':
                raise Exception('Message must start with /')

            utils.log.info(
                f"SENDING MESSAGE: {OSCMessage.MESSAGE} {OSCMessage.VALUE_ARRAY}")

            root = OSCMessage.MESSAGE.split('/')[1]

            if root != "meters" and root != "xremote" and OSCMessage.VALUE_ARRAY == b'':
                self.EXPECTED_MESSAGES.append(OSCMessage.MESSAGE)

            self.SOCK.sendto(bytes(utils.pad(OSCMessage.MESSAGE) + utils.pad(
                ',' + OSCMessage.TYPE_STRING), 'ascii') + OSCMessage.VALUE_ARRAY, (self.IP, self.PORT))

            if OSCMessage.VALUE_ARRAY == b'':

                oldTime = time.time()
                wayoldtime = time.time()

                while not self.checkMessages(self.RESULTS, OSCMessage.MESSAGE):
                    if time.time() - oldTime > 5:
                        break

                searched = self.searchResults(
                    self.RESULTS, "msg", OSCMessage.MESSAGE)

                if searched == None:
                    utils.log.error(
                        f"Couldn't find result for {OSCMessage.MESSAGE}")
                    return (0,)

                pos = self.RESULTS.index(searched)
                self.RESULTS.pop(pos)

                if searched:
                    return searched['value']
            else:
                return ()
        else:
            return (0,)

    def receive(self, msg: osc.construct, callback):
        ready = select.select([self.SOCK], [], [], self.TIMEOUT)
        print(ready)

        if ready[0]:
            data, addr = self.SOCK.recvfrom(self.HOST)

            utils.log.info(f"RECEIVED MESSAGE: {data} {addr[0]}")

            m, _ = [e for e in data.split(b',', 1) if e]

            m = m.strip(b'\x00').decode('ascii')

            if m == msg.MESSAGE:
                res = callback(data)
                return res
            else:
                utils.log.error('Unexpected packet')
                raise Exception('Observed wrong packet')
        else:
            utils.log.error('Connection timed out')
            # msg = ui.ErrorWindow(
            #     f'Connection timed out after {self.TIMEOUT} seconds')
            # msg.show()
            return (0, )

    def decode(self, data):

        _, dgram = [b',' + e for e in data.split(b',', 1) if e]

        typetag, index = types.get_string(dgram, 0)

        params = ()

        if typetag.startswith(','):
            typetag = typetag[1:]

        for type in typetag:
            match type:
                case 'i':
                    val, index = types.get_int(dgram, index)
                case 'f':
                    val, index = types.get_float(dgram, index)
                case 's':
                    val, index = types.get_string(dgram, index)
                case 'b':
                    val, index = types.get_blob(dgram, index)
                case _:
                    utils.log.error(
                        'Error in type message, recieved unknown type')
                    val, index = b'x00', index

            params += (val,)

        return params
