# import logging module
import logging
log = logging.getLogger(__name__)

# import mqtt lirary
import paho.mqtt.client as mqtt

# import control module
from implModules import controlModes

# import uility libbs
import json

class mqttClass:

    property = {}
    sensyname = ""
    controlMode = ""
    client = mqtt.Client()

    def __init__(self, sensyname, mqttProperty, controlMode, additionalOptions):
        self.sensyname = sensyname
        self.property = mqttProperty
        self.controlMode = controlMode
        self.additionalOptions = additionalOptions

        self.property["channel"] = {
            "name": "SENSY/" + self.sensyname,
            "status": self.sensyname + "/status"
        }

        log.debug("MQTT Server: %s : %s", self.property["host"], str(self.property["port"]))
        log.debug("MQTT Channel name: %s", str(self.property["channel"]["name"]))
        log.debug("MQTT Channel status path: %s", str(self.property["channel"]["status"]))
        log.info("SENSY name/id : %s", self.sensyname)
        log.debug("initializing mqttClass")

    def callControlModule(self, motion):
        log.debug("controllmode set to : %s", self.controlMode)
        if self.controlMode == "POC1":

            # if using mock, dont call setMotion and actuateMotors modules
            if self.additionalOptions["mock"]:
                log.info("[MOCKMODE] calling POC1.setMotion with motion=%s", motion)
            else:
                controlModePOC1 = controlModes.POC1()
                log.debug("calling POC1.setMotion with motion=%s", motion)
                controlModePOC1.setMotion(motion)

    def cleanup(self):
        log.info("Unsubscribing SENSY channel: %s", self.property["channel"]["name"])
        self.client.unsubscribe(self.property["channel"]["name"])
        log.info("Disconnecting MQTT connection")
        self.client.disconnect()

    # def to call when connected
    def onConnect(self, client, data, flag, rc):
        if rc == 0:
            log.info("MQTT connected")
            log.debug("MQTT Connect code: %s", rc)

            # subscribe to the channel
            self.client.subscribe(self.property["channel"]["name"])
            log.info("subscribed to channel %s", self.property["channel"]["name"])
        else:
            log.warning("MQTT Connection failed with code: %s", rc)

    # def to call when recieved a message
    def onMessage(self, client, data, msg):
        payloaddata = json.loads(str(msg.payload.decode("utf-8")))
        log.debug(payloaddata)
        if "actionMode" in payloaddata:
            log.debug("payloaddata has actionMode")
            if payloaddata["actionMode"] == "setMotion":
                log.debug("setMotion value is : %s", payloaddata['setMotion']['value'])
                self.callControlModule(payloaddata['setMotion']['value'])

    def startCommunication(self):
        log.info("Starting MQTT comunication")
        self.client.username_pw_set(username=self.property["auth"]["username"], password=self.property["auth"]["password"])
        self.client.on_connect = self.onConnect
        self.client.on_message = self.onMessage
        self.client.will_set(self.property["channel"]["status"], b'{"status": "off"}')
        log.debug("connecting to mqtt broker %s : %s", self.property["host"], self.property["port"])
        self.client.connect(self.property["host"], self.property["port"], self.property["timeout"])
        log.info("MQTT Connected, now listening")
        self.client.loop_forever()
