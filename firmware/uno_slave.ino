
#include <Wire.h>               // library to communicate with i2c devices

#define SLAVE_ADDRESS 0x00      // i2c slave address

int fuelSensorPin = 0;          // pin definitions
int relay1Pin = 3;
int relay2Pin = 5;
int rpiPowerPin = 7;

float fuelSensorVal = 0;        // variable to store sensor value
int response[2] = {0,0};        // variable to store i2c response to send
int receivedData = 0;           // variable to store received data from i2c 

unsigned int i2cTime= 0;        // variable to track last i2c communication time


void setup() {
    
    Wire.begin(SLAVE_ADDRESS);          // initialize i2c

    Wire.onReceive(receive);            // define callbacks for i2c communication
    Wire.onRequest(respond);

    pinMode(relay1Pin, OUTPUT);         // set pin modes for controls
    pinMode(relay2Pin, OUTPUT);
    pinMode(rpiPowerPin, OUTPUT);
    
    digitalWrite(rpiPowerPin, HIGH);    // power up RPI
}


void loop() {
    
    if (millis() - i2cTime  > 10000) {      // if no i2c communication in 10 seconds
        digitalWrite(rpiPowerPin, LOW);     // reset RPI
        delay(1000);                    
        digitalWrite(rpiPowerPin, HIGH); 
        i2cTime = millis();
        }
        
    delay(10); 
}


// callback for receiving data
void receive(int byteCount){
    i2cTime = millis();                     // update counter since i2c communication received
    
    receivedData = Wire.read();

    switch(receivedData) {
        case 1  :
            digitalWrite(relay1Pin, HIGH);    //turn relay 1 on
            break; 
        case 2  :
            digitalWrite(relay2Pin, HIGH);    //turn relay 2 on
            break; 
        case 3  :
            digitalWrite(relay1Pin, LOW);     //turn relay 1 off
            break; 
        case 4  :
            digitalWrite(relay2Pin, LOW);     //turn relay 2 off
            break;     
        case 5  :
            fuelSensorVal = analogRead(fuelSensorPin);              // read fuel sensor
            fuelSensorVal = fuelSensorVal * (5.0 / 1023.0);         // change the value to voltage
            fuelSensorVal = fuelSensorVal*100;                      // change the value to unit of 0.01V
            response[0] = fuelSensorVal/100;                        // send first two digits as LSB
            response[1] = fuelSensorVal - (fuelSensorVal/100)*100;  // send last 2 digits as MSB
            break;    
    }
}


// callback for sending response
void respond(){
    Wire.write(response[0]);
    Wire.write(response[1]);
}
