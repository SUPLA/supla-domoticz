# Docker
## Create new image
```sh
docker build -f supla_dev/Dockerfile -t supla-domoticz-test .
```
## Start container
```sh
docker run --name=supla-domoticz-test \
        --privileged \
        --cidfile="cid" \
        -d \
        -p 7070:8080 \
        -p 7071:9090 \
        -t supla-domoticz-test
```
To validate if Domoticz is running visit http://localhost:7070

To validate id jSuplaServerMock is running do this:
```sh
curl -X GET "http://localhost:7071/api/v2.3.0/server-info" -H  "accept: application/json"
```
