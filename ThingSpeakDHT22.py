import Adafruit_DHT #provide access to DHT sensor function
from time import time, sleep #shows time in visualization
from urllib.request import urlopen #opens url(HTTP)
import sys #provide access to required variables/functions

WRITE_API = "Your ThingSpeak Write API" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API) #transfering sensor signal to thingspeak

buzzer = Buzzer(26) #buzzer tone

SENSOR_PIN = 4 # number of pins of DHT22
SENSOR_TYPE = Adafruit_DHT.DHT22 # Type of sensor

SensorPrevSec = 0
SensorInterval = 2 # 2 seconds detecting interval for the sensor
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds, as 15 seconds of transfering data to thingspeak is the minimum for free thingspeak account

# Code to show signal data in temperature and humidity in console and visualize in thingspeak
try:
    while True:
        
        if time() - SensorPrevSec > SensorInterval:
            SensorPrevSec = time()
            
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
            print("Humidity = {:.2f}%\tTemperature = {:.2f}C".format(humidity, temperature))
        
        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}".format(temperature, humidity)
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            
            sleep(1)
            
