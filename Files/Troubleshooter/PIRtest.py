import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer
from gpiozero import LED
from gpiozero import MotionSensor


led = LED(18)
buzzer = Buzzer(13)
pir = MotionSensor(0)

while True:
    time.sleep(2)
    i=pir.value
    
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        led.off()  #Turn OFF LED
        time.sleep(0.5)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        led.on()  #Turn ON LED
        time.sleep(1)