# CMIDAT01K_IOT_Temperature-HumidityDectector
## Story
Living underground is notoriously known for its high humidity and temperature in the summer. As a student, I tend to opt for cheaper room to live in. Thus, living in a bedroom under the ground level of an apartment with tiny windows and sub-standard ventilation system is common. Especially in the summer, the living condition can get quite unbearable when the air in underground living spaces get warmer and warm air "holds" more moisture, hence the humidity gets higher. This IoT project is made to improve the living condition of underground bedroom in the summer by monitoring the humidity and temperature of the bedroom remotely. Then, ventilating the air in the underground bedroom wirelessly, thus increase air circulation in the room to prevent stagnant summer air that holds moisture and heat.
The idea behind this project is to implement a humidity and temperature detector, dht22 with a Raspberry Pi 3 and visualize the data into ThingSpeak. With the help of ThingSpeak, the condition of the air in underground bedroom can be monitered. This is even more convinent with ThingView being installed on mobile phone, where accessing the readings of humidity and temperature in the underground bedroom is just a touch away. Then a mechanical fan can be wirelessly set to on/off by using a smart plug, TP-Link HS110. Hence starting to ventilate the bedroom when the temperature and humidity in the room is deemed uncomfortable to be inside.
## Pipeline of this IoT Project
Pipeline of this IoT project can be found in file:"My_IoT_Pipeline.png". The pipeline diagram depicts the problem narrated in the "Story" paragraph to solution of it.

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
### Overview of DHT22 
DHT22 is a sensor which ables to detect humidity in % and temperature in °C. Refer to file:"DHT22 with numbered pinsDHT22.png" for pins numbering. Pinout descriptions are as follows:
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

### Preparing the fan 
Plug in the smart plug into a socket and connect it to Wifi with Kasa app. Then, plug in the fan into smart plug. Once it's connected, the fan can remotely switch on/off.

Now, the hardwares are all connected and the next software setup can be proceeded.

## Software Setup
To setup your new Raspberry Pi, refer to "THE OFFICAL Raspberry Pi Beginner's Guide, Chapter 2". 
1. Once it's all set and ready, let's proceed to updating the Raspberry Pi by running the following commands:
* sudo apt-get update
* sudo apt-get upgrade
2. Now, let's install both python 3 and pip with the following command:
* sudo apt-get install python3-dev python3-pip
3. Then, update the setuptools, wheel and pip of python packages to the latest version:
* sudo python3 -m pip install --upgrade pip setuptools wheel
4. Lastly, using pip to install Adafruit's DHT library to Raspberry Pi by writing the following command in the terminal. This allows Python library to interact with DHT22. 
* git clone https<span>://</span>github.com/adafruit/Adafruit_Python_DHT.git
* sudo python3 setup.py install

## Preparing ThingSpeak
1. Sign-up with a mathwork account.
2. Make a channel and name it with "Raspberry Pi + DHT22 Temperature & Humidity Sensor".
3. Name Field 1 with Temperature (°C) and Field 2 with Humidity (%).
4. Get API Keys from "Write API Key" in menu tab "API KEYS". This API key will be used in the code of the following section.

## Programming
Thonny Python IDE is used in this project to run the codes. The codes with comments can be found in ThingSpeakDHT22.py in this repository. Do take note that API key has to be adapted to the one found in created thingspeak's channel. The is recommended to run for error check and a result in Python console should be shown as such in file:"Python_console_readings.png". Then go into thingspeak channel:"Raspberry Pi + DHT22 Temperature & Humidity Sensor" to see the visualized data. 

## Visualization of Data on ThingSpeak
Refer to file: 

## Viewing the visualization on your Phone
To access the visualized signal data on your phone, it can be done either by accessing thingspeak.com with phone's browser or through Thingview app. This can be easily done by installing Thingview app onto phone and sign in with Thingspeak account. Then key in the channel id of "Raspberry Pi + DHT22 Temperature & Humidity Sensor". Figure in file:"xxxx" shows the visualisation of humidity and temperature readings in the underground bedroom with time as x-axis. 

## Video
Refer to file:"xxxxx".
The video shows the pipeline of this IoT project and a simulation experiment is done to test the feasibility of this IoT project. The summer summer condition in the underground bedroom is simulated by turning on heater to warm up the room. Then, after the 5 minutes mark, fan is switched on remotely using Kasa app and the temperature and humidity in the room are monitored with both Python script and ThingSpeak visualization. turn on the heater to higher


## Recommendation:
This project could be done better if HS110 is integrated directly into Raspberry Pi 3 to automate the mechanical fan when an uncomfortable living condition in terms of humidity and tempeature is detected in the room. 
