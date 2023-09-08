import socket, struct, math, threading, select, time, queue
from OSC import OSC, ConstructOSCMessage 

# WIRESHARK FILTER:
# ip.src == 127.0.0.1 and udp and ip.dst == 127.0.0.1 and not icmp

if __name__ == "__main__":
    osc = OSC('127.0.0.1')

    while True:
        gain = osc.send(ConstructOSCMessage('/ch/01/mix/fader', {'f': 0.8250}))[0]
        print(gain)
        time.sleep(0.1)

    # funny fader thing
    # x = True
    # while True:
    #     for i in range(16):
    #         print(str(i+1).zfill(2))
    #         time.sleep(0.05)
    #         res = osc.send(ConstructOSCMessage(f'/ch/{str(i+1).zfill(2)}/mix/fader'))
    #         print(res)
    #     x = not x
