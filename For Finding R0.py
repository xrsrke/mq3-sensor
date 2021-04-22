"""
FOR FIND R0

- Created by Anas Ahmed - Hackerspace Karachi
- anas.ahm5@gmail.com - hackerspacekarachi.org
- Whatsapp: +92 332 3265201


LIBRARIES:
- SPIDEV
sudo pip3 install spidev
- NUMPY
sudo pip3 install numpy
-WIRINGPI
sudo pip3 install wiringpi

"""

import spidev              
from numpy import interp    
from time import sleep	   
import RPi.GPIO as GPIO	   


spi = spidev.SpiDev() 
spi.open(0,0)	


GPIO.setmode(GPIO.BCM)

R2 = toint(input("Enter R2 value : "))

 
#MCP3204
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while True:
    value = analogInput(0)  # 0 for CH0
    #print( "RAW VALUES:", values)

    sensor_volt= tofloat(value/1024*5.0)
    RS_gas = ((5.0 * R2)/sensor_volt) - R2
    R0 = RS_gas / 60
    print("R0: ", R0)
  
    sleep(0.05)
  
