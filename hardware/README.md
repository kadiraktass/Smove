# Hardware challenge solution  


[Desired hardware](https://github.com/itatsmove/smovechallenge/blob/master/challenges/hardware.md) is designed using [Eagle 9.1.0](https://www.autodesk.com/products/eagle/overview). Design files, BOM and Gerber files are included in [uno_sensor_shield](https://github.com/kadiraktass/Smove/tree/master/hardware/uno_sensor_shield) folder. 

Arduino Uno shield package is used for board outline and arduino pins. Board is built on this object.  

I2C signals are pulled up and passed through a bidirectional 5v-3v3 voltage level shifter before connecting to ICs.  

All the parts used in the design and battery cell holder and headers for Arduino are included in BOM. 

PCB has two layers, top and bottom. Both layers are filled with Ground. 

Power lines are drawn thicker compared to signal lines. 

Design can be changed to provide certain requirements such as dimensions.  

## Libraries 

The following libraries are used for missing footprints:  
[MPU9250](https://componentsearchengine.com/MPU-9250/InvenSense+Inc.)  
[OPT3001](https://componentsearchengine.com/part.php?partID=300356)  
[PCF8523T](https://componentsearchengine.com/part.php?partID=274221)  
[BMP280](https://componentsearchengine.com/part.php?partID=237787)  
[CR1220 and Uno Shield Package](https://github.com/adafruit/Adafruit-Eagle-Library)  
[BSS138](https://componentsearchengine.com/part.php?partID=232961)  
[JTX210](https://componentsearchengine.com/part.php?partID=1253227)  


