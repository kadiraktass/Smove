## Firmware challenge solution

[Desired system](https://github.com/itatsmove/smovechallenge/blob/master/challenges/firmware.md) is implemented by two scripts. [One](https://github.com/kadiraktass/smove/blob/master/firmware/uno_slave.ino)(uno_slave.ino) for Arduino and [one](https://github.com/kadiraktass/smove/blob/master/firmware/rpi_master.py)(rpi_master.py) for Raspberry Pi. 

# Rpi script 

In the main loop, Rpi gets the commands from the user via serial interface. Then it orders Arduino to perform a task according to the command it gets from the user. And, it responses to the user accordingly. 

In another thread, Rpi reads the fuel sensor value periodically by sending a request to Arduino in every second. 


Communication between Rpi and Arduino is established with I2C as Rpi master. A simple command list is defined for the purpose of message exchange between these two device. 

Used libraries in Rpi script: 
[Pyserial](https://pythonhosted.org/pyserial/) (For the serial interface)
[Smbus](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/i2c/smbus-protocol) 

