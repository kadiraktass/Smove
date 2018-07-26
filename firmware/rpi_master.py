#!/usr/bin/python
import serial           # for UART
import smbus            # for I2C 
import threading        # for periodic sensor check

# define I2C address for arduino
address = 0x00

# define UART port name and baudrate
uartPortName = "/dev/tty-ACM0"      
baudRate = 115200

# initialize variable to store fuel sensor reading
sensorValue = 0

# define function to check fuel sensor periodically    
def checkSensor(): 

    i2c.write_byte(address, arduinoCommands["AT+SENS=?"])        # command Arduino to get sensor's value
    arduinoRsp = i2c.read_i2c_block_data(address, 0,2)           # Arduino sends sensor value in two bytes but as int digits
    sensorValue = arduinoRsp[0]*100+arduinoRsp[1]                # combine to obtain the reading
    threading.Timer(1, checkSensor).start()                      # check every second

    
# define functions to carry out the UART terminal commands 
def setRelay(command): 

    i2c.write_byte(address, arduinoCommands[command])           # command Arduino to control the relays 
    return "^OK\r\n"                                            # return the response

def readSensor(command):
    return "^OK\r\n" + str(sensorValue) + "\r\n"                # return the response with last fuel sensor read value 

    
# map the UART terminal commands to the respective functions
uartCommands = {
                "AT+RLYON=1"  : setRelay,
                "AT+RLYON=2"  : setRelay,
                "AT+RLYOFF=1" : setRelay,
                "AT+RLYOFF=2" : setRelay,
                "AT+SENS=?"   : readSensor,
           }

# values to be send to Arduino for each command, Arduino operates according to the value it receives
arduinoCommands = {
                "AT+RLYON=1"  : 1,
                "AT+RLYON=2"  : 2,
                "AT+RLYOFF=1" : 3,
                "AT+RLYOFF=2" : 4,
                "AT+SENS=?"   : 5,
                }
                
# define a function to read a line from UART terminal                 
def readLine(port):
    receivedLine = ""
    while True:
        receivedChar = port.read()                  
        receivedLine += receivedChar
        if receivedChar=='\r' or receivedChar=='':
            return receivedLine

# initialize the I2C bus
i2c = smbus.SMBus(0)

# initialize the UART terminal
uartPort = serial.Serial(uartPortName, baudRate)

# send reset response to UART terminal as script starts
uartPort.write("^RESET\r\n")

# start periodic sensor check
checkSensor()
 
while True:
    receivedCommand = readLine(uartPort)                # read the UART terminal command
    
    if receivedCommand in uartCommands:                             # check if the received UART terminal command is valid 
        rpiRSP = uartCommands[receivedCommand](receivedCommand)     # process the command 
        uartPort.write(rpiRSP)                                      # send the response to UART terminal
    else: 
        uartPort.write("Invalid command\r\n")

        
        
