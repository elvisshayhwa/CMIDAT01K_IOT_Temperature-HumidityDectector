# CMIDAT01K_IOT_Temperature-HumidityDectector
## Story
Living underground is notoriously known for its high humidity and temperature in the summer. As a student, I tend to opt for cheaper room to live in. Thus, living in a bedroom under the ground level of an apartment with tiny windows and sub-standard ventilation system is common. Especially in the summer, the living condition can get quite unbearable when the air in underground living spaces get warmer and warm air "holds" more moisture, hence the humidity gets higher. This IoT project is made to improve the living condition of underground bedroom in the summer by monitoring the humidity and temperature of the bedroom remotely. Then, ventilating the air in the underground bedroom wirelessly, thus increase air circulation in the room to prevent stagnant summer air that holds moisture and heat.
The idea behind this project is to implement a humidity and temperature detector, dht22 with a Raspberry Pi 3 and visualize the data into ThingSpeak. With the help of ThingSpeak, the condition of the air in underground bedroom can be monitered. This is even more convinent with ThingView being installed on mobile phone, where accessing the readings of humidity and temperature in the underground bedroom is just a touch away. Then a mechanical fan can be wirelessly set to on/off by using a smart plug, TP-Link HS110. Hence starting to ventilate the bedroom when the temperature and humidity in the room is deemed uncomfortable to be inside.

## Things needed
### Hardware components
- Raspberry Pi 3
- 8GB or more Micro SD Card
- Breadboard 
- 3x F-M jumpwires & 1x M-M jumpwire
- DHT22 Humidity and Temperature sensor
- 10k ohm resistor (For easier identification, stripe color: Brown, Black, Orange, Gold)
- Smart plug, HS110
- Fan

### Software
- Python 3
- ThingSpeak 
- ThingView app (easier access with mobile phone for monitoring of humidity and temperature)
- Kasa app (controlling smart plug)

## Hardware Setup
In this section, the process of connecting DHT22 sensor to Raspberry Pi is described
### Overview of DHT22 (refer to diagram of DHT22 with numbered pins)
DHT22 is a sensor which ables to detect humidity in % and temperature in °C. DHT22 pinout descriptions are as follows:
- Pin 1 = VCC, power supply
- Pin 2 = SDA, data out
- Pin 3 = N/C, do not connect
- Pin 4 = GND, ground
### DHT22 and Pi Circuit
Steps to connect DHT22 to Raspberry Pi are described in this section. A circuit diagram can be found in the respiratory:"Circuit of DHT22 and Pi.PNG"
1. Place DHT22 at the top row of breadboard.
2. Place a 10k resistor between Pin 1 Pi and Pin 2 DHT22.
3. Wire Physical Pin 1 Pi(3v3 power) to Pin 1 DHT22. (refer to red wire and blue wire)
4. Wire Physical Pin 7 Pi(GPIO 4) to Pin 2 DHT22. (refer to green wire)
5. Wire Physical Pin 6 Pi to Pin 4(Ground) DHT22. (refer to black wire)

Then, plug the fan into the smartplug. 
Now, the hardwares are all connected and the next software setup can be proceeded.

## Software Setup
To setup your new Raspberry Pi, refer to "THE OFFICAL Raspberry Pi Beginner's Guide, Chapter 2". 
1. Once it's all set and ready, let's proceed to updating the Raspberry Pi by running the following commands:
* sudo apt-get update
* sudo apt-get upgrade
2. Now, let's install both python 3 and pip with the following command:
* sudo apt-get install python3-dev python3-pip
3. Then, update the setuptools, wheel and pip of python packages to the latest version:
* sudo python3 -m pip install - upgrade pip setuptools wheel
4. Lastly, using pip to install Adafruit's DHT library to Raspberry Pi by writing the following command in the terminal. This allows Python library to interact with DHT22. 
* git clone https://github.com/adafruit/Adafruit_Python_DHT.git
* cd Adafruit_Python_DHT
* sudo python3 setup.py install

## Preparing ThingSpeak
1. Sign-up with a mathwork account
2. Make a channel and name Field 1 with Temperature (°C) and Field 2 with Humidity (%)
3. Get API Keys from "Write API Key" in menu tab "API KEYS". This API key will be used in the code of the following section.

## Programming
Thonny Python IDE is used in this project to run the codes. The codes with comments can be found in ThingSpeakDHT22.py in this respository. Do take note that API key has to be adapted to the one found in created thingspeak's channel.

Recommendation:
This project could be done better if HS110 is integrated directly into Raspberry Pi 3 to automate the mechanical fan when an uncomfortable living condition in terms of humidity and tempeature is detected in the room. 
