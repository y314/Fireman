
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
import webrepl
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

def do_connect(ssid, pwd,dname):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network:{} as device:{}...'.format(ssid,dname))
        sta_if.active(True)
        sta_if.config(dhcp_hostname=dname)
        sta_if.connect(ssid, pwd )
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    webrepl.start()
 
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
 
# Attempt to connect to WiFi network
import json
with open("conf.json") as config:
    config_data = json.load(config)

print ("Connecting {}".format (config_data["wifi"]["ssid"]))
ssid=config_data["wifi"]["ssid"]
pss= config_data["wifi"]["pss"]
dname= config_data["wifi"]["dname"]
do_connect(ssid, pss, dname)


 



