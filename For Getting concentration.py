"""
Getting values in mg/L

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

R2 =          #"Enter R2 value"
R0 =          #"Enter R0 value"
 
#MCP3204
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while True:
    value = analogInput(0)  # 0 for CH0
    #print( "RAW VALUES:", values)

    sensor_volt= sensorValue/1024*5.0
    RS_gas = ((5.0 * R2)/sensor_volt) - R2
    ratio = RS_gas/R0
    x = 0.4*ratio;   
    BAC = pow(x,-1.431)       #BAC in mg/L
    print("BAC = ", BAC)

    #print(BAC*0.0001)  //convert to g/dL

  
    sleep(0.05)

    
