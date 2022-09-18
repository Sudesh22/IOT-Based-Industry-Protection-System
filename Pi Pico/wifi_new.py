from machine import UART, Pin
import time
from esp8266 import ESP8266

esp01 = ESP8266()
uart = UART(0,115200)

esp8266_at_ver = None
led=Pin(25,Pin.OUT)

device_id = 1
host_ip = "192.168.0.105"
port = "5000"
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

print("StartUP",esp01.startUP())
print("Echo-Off",esp01.echoING())
print("\r\n")

esp8266_at_var = esp01.getVersion()
if(esp8266_at_var != None):
    print(esp8266_at_var)

esp01.setCurrentWiFiMode()

print("Try to connect to the WiFi..")
send='AT+CWJAP="Manjrekar","15atharva07"'
uart.write(send+'\r\n')
time.sleep(5)
print("\r\n")
print("starting HTTP Get/Post Operation.......\r\n")

while(1):
    led.toggle()
    time.sleep(1)
    
    reading_temp = sensor_temp.read_u16() * conversion_factor 
    temperature = str(int(27 - (reading_temp - 0.706)/0.001721))
    
    httpCode, httpRes = esp01.doHttpGet(host_ip,"/2","RaspberryPi-Pico", port)
    print("------------- Get Operation Result on 192.168.0.105:5000/2 ------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n\r\n")
    
    #post_json="{\"name\":\"Noyel\"}"
    #httpCode, httpRes = esp01.doHttpPost(host_ip,"/","RPi-Pico", "application/json",post_json,port)
    #print("---------------- Post Operation Result on 192.168.0.105:5000/ ------------------")
    #print("HTTP Code:",httpCode)
    #print("HTTP Response:",httpRes)
    #print("--------------------------------------------------------------------------------\r\n\r\n")
    
    post_json="{\"data\":\"Temperature:\"}"
    httpCode, httpRes = esp01.doHttpPost(host_ip,"/","RPi-Pico", "application/json",post_json,port)
    print("---------------- Post Operation Result on 192.168.0.105:5000/ ------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("--------------------------------------------------------------------------------\r\n\r\n")