"""
<plugin key="supla" name="Supla" author="Supla Team" version="0.1.0" externallink="https://supla.org/">
    <description>
        <h2>Supla Plugin</h2>
        <br/>
        <h3>Devices</h3>
        <ul style="list-style-type:square">
            <liv>Switches &amp; lights</liv>
            <liv>RGB and dimmer controllers</liv>
            <liv>Temperature &amp; humidity devices</liv>
            <liv>Gates (and sensors)</liv>
            <liv>Roller shutter controllers</liv>
        </ul>
        <h3>Configuration</h3>
        <ul style="list-style-type:square">
            <li>oAuth Token</li>
            <li>Device GUID</li>
        </ul>
    </description>
    <params>
        <param field="Mode2" label="Device GUID" required="true"/>
        <param field="Mode1" label="oAuth Token" required="true"/>
        <param field="Mode1" label="Refresh Interval (seconds)" required="true" defualt="30"/>
    </params>
</plugin>
"""
import Domoticz


class BasePlugin:
    enabled = False

    def __init__(self):
        # self.var = 123
        return

    def onStart(self):
        Domoticz.Debug("onStart called")

    def onStop(self):
        Domoticz.Debug("onStop called")

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")

    def onMessage(self, Connection, Data):
        Domoticz.Debug("onMessage called")

    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Debug(
            "onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level))

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Debug("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(
            Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        Domoticz.Debug("onDisconnect called")

    def onHeartbeat(self):
        Domoticz.Debug("onHeartbeat called")


global _plugin
_plugin = BasePlugin()


def onStart():
    global _plugin
    _plugin.onStart()


def onStop():
    global _plugin
    _plugin.onStop()


def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)


def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)


def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)


def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)


def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)


def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

    # Generic helper functions


def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug("'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
