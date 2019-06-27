FROM joshuacox/mkdomoticz
RUN apt-get update && apt-get install -y curl default-jre

# Run jSupla Server Mock
WORKDIR /
RUN curl -L "https://dl.bintray.com/big-boy/bigboy/pl/grzeslowski/jsuplaservermock/jsupla-mock-server/0.9.14/jsupla-mock-server-0.9.14.jar" -o jsuplaservermock.jar
COPY supla_dev/docker-start-domoticz.sh /
RUN chmod +x docker-start-domoticz.sh
EXPOSE 9090

# Copy actual plugin to Domoticz plugins
WORKDIR /src/domoticz/plugins/
COPY plugin.py supla-domoticz/
COPY supla_api supla-domoticz/supla_api

WORKDIR /
CMD [ "/docker-start-domoticz.sh" ]
