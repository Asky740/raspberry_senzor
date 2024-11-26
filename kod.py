from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT11(Pin(1))

led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(5, Pin.OUT)

while True:
    sleep(0.1)
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("------------------")
        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %hum)
        if 0 < hum < 25:
            led1(True)
            led2(False)
            led3(False)
            led4(False)
        elif 25 < hum < 50:
            led1(True)
            led2(True)
            led3(False)
            led4(False)
            sleep(2)
        elif 50 < hum < 75:
            led1(True)
            led2(True)
            led3(True)
            led4(False)
        elif 75 < hum < 100:
            led1(True)
            led2(True)
            led3(True)
            led4(True)

    except OSError as e:
        print('Failed to read sensor.')