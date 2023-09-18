# Will Baker Computer Science Coursework

## Testing

If you dont have an X32, you can either use the X32 Simulator by Patrick-Gilles Maillot which you can download [here](https://sites.google.com/site/patrickmaillot/x32#h.p_rE4IH0Luimc0), or simply observe the packets being sent using the Wireshark filter:

`ip.src == 127.0.0.1 and udp and ip.dst == 127.0.0.1 and not icmp`