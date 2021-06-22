__author__      = "Yaniv Dadon"
__copyright__   = "Copyright 2021, 72k.co.il"

from machine import Pin, ADC
from time import sleep, sleep_ms

from max6675 import MAX6675
import urequests as requests
import json
import machine
import ubinascii

#from time import sleep_ms

MachineName = ubinascii.hexlify(machine.unique_id()).decode('utf-8')

led=Pin(2,Pin.OUT)

sd1=ADC(Pin(34)) #MQ2
sd1.atten(ADC.ATTN_11DB)

sd2=ADC(Pin(35)) #MQ5
sd2.atten(ADC.ATTN_11DB)

so = Pin(12, Pin.IN)
cs = Pin(16, Pin.OUT)
sck = Pin(14, Pin.OUT)


max = MAX6675(sck, cs , so)


def status():
    status={"MQ2":sd1.read(),"MQ5":sd2.read(),
    "TC":max.read(),"MID" : MachineName,}
    return status


def getValues():
    mydata=json.dumps(status())
    header= {'content-type': 'application/json'}
    try:
        r= requests.post('http://rest.72k.co.il', data = mydata, headers = header)
        print(r.text)
    except OSError:
        bk(iserr=1)
    
def st(cnt=500):
    i=0
    while i<cnt:
        i+=1
        print(status())
        sleep(0.5)

def bk(iserr=0):
    t=1
    if iserr ==0:
        while t<10:
            led.on()
            sleep_ms(40)
            led.off()
            sleep_ms(40)
            t+=1
        led.off()
    else:
        while t<3:
            led.on()
            sleep(1.5)
            led.off()
            sleep_ms(40)
            t+=1
            #led.off() 

def report(cnt=2880):
    i=0
    while i<cnt:
        i+=1
        getValues()
        sleep(10)
    led.on()

bk()
report()
