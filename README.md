***

<div align="center">
    <b><em>Supla ❤️ Domoticz</em></b><br>
</div>

<div align="center">
	
[![Build Status](https://travis-ci.org/SUPLA/supla-domoticz.svg?branch=master)](https://travis-ci.org/SUPLA/supla-domoticz)

</div>

***

# (IoT) Internet of Things is now coming!

Building automation systems available on the market are usually very complex, closed and expensive. In many cases they 
must be installed on the very early stages of house construction. SUPLA is simple, open and free of charge. It gives an 
opportunity to build elements based on RaspberryPI, Arduino or ESP8266 platforms and then join them either through LAN 
or WiFi. Through SUPLA you can, among others, control the lighting, switch on and off household appliances and media, 
open and shut gates and doors, or control room temperature. All the above can be done with just touch of a finger. SUPLA 
is available from any place on Earth if you just have a smartphone or tables available as well as Internet access. SUPLA 
is developed based on an Open Software and Open Hardware . This way, you can also develop this project!  - <a href="https://supla.org">Supla</a>

## SUPLA-CLOUD

SUPLA-CLOUD is a central point joining the executive devices for indirect and direct operation of your household or office appliances and other elements with client applications which you can install on your tablets and smartphones. This software allows to operate, from one spot, the whole system infrastructure using any modern Internet browser. Server access is free of charge. You can also set up your own independent server working within the Internet or home network using system sources which you can download from GITHUB.

<a href="https://cloud.supla.org/account/create">Create an account</a>
<a href="https://github.com/SUPLA">Get from GITHUB</a>

# Development
## Docker
### Create new image
```sh
docker build -f supla_dev/Dockerfile -t supla-domoticz-test .
```
### Start container
```sh
docker run --name=supla-domoticz-test \
        --privileged \
        -d \
        -p 7070:8080 \
        -p 7071:9090 \
        -t supla-domoticz-test
```
To validate if Domoticz is running visit http://localhost:7070

To validate if `jSuplaServerMock` is running do this:
```sh
curl -X GET "http://localhost:7071/api/v2.3.0/server-info" -H  "accept: application/json"
```
