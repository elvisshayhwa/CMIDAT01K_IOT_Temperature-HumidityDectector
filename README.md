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
### Overview of DHT22 
DHT22 is a sensor which ables to detect humidity in % and temperature in °C. DHT22 


Recommendation:
This project could be done better if HS110 is integrated directly into Raspberry Pi 3 to automate the mechanical fan when an uncomfortable living condition in terms of humidity and tempeature is detected in the room. 
