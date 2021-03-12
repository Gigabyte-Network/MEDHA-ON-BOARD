import os
import sys

# append utils path and import utils modules
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "utils"))
import LogModule
import Configs

# append utils path and import utils modules
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "localization"))
import readUltraSonicSensor

log = LogModule.init_logger()
config = Configs.configValues()

class ultrasonicSensor:
    mock = False
    def __init__(self, ultrasonicSensors, options):
        self.ultrasonicSensors = ultrasonicSensors
        if (("mock" in options) and (options["mock"])):
            # set mock if specified and mock is passed True
            self.mock = options["mock"]

    def getValue(self, ultrasonicSensorName):
        # read value from readUltraSonicSensor module
        russ = readUltraSonicSensor.readUltraSonicSensor({
            "mock": self.mock
        })
        return russ.readSensorValue(ultrasonicSensorName)





########## Mock function ##########
if (( config.property["mock"]["isMock"] ) and (__file__ == "readSensor.py")):
    # init class object with options
    uss = ultrasonicSensor(config.pins["sensors"]["ultrasonic"], {
        "mock": config.property["mock"]["isMock"]
    })

    # check the value responses with left and right
    numOfTimes = 10

    # right
    pinToReadFrom = "right01"
    for num in range(numOfTimes):
        log.info("MOCK: PIN:%s | %s", pinToReadFrom, uss.getValue(pinToReadFrom))

    # left
    pinToReadFrom = "left01"
    for num in range(numOfTimes):
        log.info("MOCK: PIN:%s | %s", pinToReadFrom, uss.getValue(pinToReadFrom))

    # front
    pinToReadFrom = "front01"
    for num in range(numOfTimes):
        log.info("MOCK: PIN:%s | %s", pinToReadFrom, uss.getValue(pinToReadFrom))
