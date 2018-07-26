# Firmware challenge solution

[Desired system](https://github.com/itatsmove/smovechallenge/blob/master/challenges/firmware.md) is implemented by two scripts. [One](https://github.com/kadiraktass/smove/blob/master/firmware/uno_slave.ino) (uno_slave.ino) for Arduino and [one](https://github.com/kadiraktass/smove/blob/master/firmware/rpi_master.py) (rpi_master.py) for Raspberry Pi. 

## Installation instructions

You need to activate I2C interface on your RPi. Open a terminal window in RPi. Run:

    sudo raspi-config
    
Go to **5 Interfacing Options**. Select **I2C** and select **Yes**.  
Also, you need to install libraries for I2C if they are not installed yet. In the terminal, run:

    sudo apt-get install python-smbus i2c-tools  
    


## Usage 

## RPi script 

In the main loop, RPi gets the commands from the user via serial interface. Then it process the command by either ordering Arduino to perform a task or getting the last fuel sensor read value. And, it responses to the user accordingly. 

In another thread, RPi reads the fuel sensor value periodically by sending a request to Arduino in every second. 

Communication between RPi and Arduino is established with I2C as RPi master. A simple command list is defined for the purpose of message exchange between these two device. 

Used libraries in RPi script: 
[Pyserial](https://pythonhosted.org/pyserial/) (For the serial interface)
[Smbus](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/i2c/smbus-protocol) (For I2C)
[Threading](https://docs.python.org/3/library/threading.html) (For periodic check) 


