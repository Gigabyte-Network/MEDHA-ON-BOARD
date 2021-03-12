# import libraries
import argparse
import logging
import os
import json

# init CLI arg parameters
parser = argparse.ArgumentParser()
parser.add_argument("-cm", "--connectmode", help="connection mode to connect to this SENSY", default="MQTT")
parser.add_argument("-sn", "--sensyname", help="name or id of the sensy", default="SENSY_P01")
parser.add_argument("-mb", "--MQTTBrokerHost", help="MQTT Broker host/ip", default="10.0.0.110")
parser.add_argument("-mp", "--MQTTBrokerPort", help="MQTT Broker port", default=1883, type=int)
args = parser.parse_args()

# init log module
logging.basicConfig(
    format='%(asctime)-15s - %(levelname)8s - %(module)10s - %(message)s',
    level=logging.DEBUG,
    datefmt='%m/%d/%Y %I:%M:%S.%p',
    handlers=[
        logging.FileHandler("sensy.log"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)


# define variables
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PROPERTY_FILE = CURRENT_DIR + "/properties.json"

with open(PROPERTY_FILE) as property:
    # use property for properties from file
    property = json.load(property)

    if property["SENSY"]["connectionMode"] == "MQTT":
        # import mqttLib
        from implModules import mqttLib

        options = {
            "mock": property["mock"]
        }

        mqtt = mqttLib.mqttClass(property["SENSY"]["name"], property["MQTT"], property["SENSY"]["controlMode"], options)
        try:
            mqtt.startCommunication()
        except KeyboardInterrupt as ke:
            log.warning(ke)
        finally:
            mqtt.cleanup()
