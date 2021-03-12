import time
import signal
import sys
import sched
import threading
import atexit
import localization.readSensor as readSensor
import localization.directionDecisions as directionDecisions
import utils.LogModule as LogModule
import utils.Configs as Configs
import utils.SignalHandler as signalHandler
import tasks.basicChecks as bc
import tasks.exitChecks as ec

log = LogModule.init_logger()
config = Configs.configValues()

options = {
    "minDistance": 60,
    "sleep": 1,
    "bgTaskTimer": 2
}

# run background jobs if any
# define background tasks defs
def startBackgroundTasks():
    log.info("[startBackgroundTasks] Thread started in background [ name: %s | identity: %s ]", threading.current_thread().name, threading.get_ident())
    bc.basicChecks(options["bgTaskTimer"]).basicChecks1()



def startAutonomy(goAhead):
    # init sensor modules
    ultrasonicSensor = readSensor.ultrasonicSensor(config.pins["sensors"]["ultrasonic"], { "mock": config.property["mock"]["isMock"] })
    dDecisions = directionDecisions.basicDecision(config.property["MEDHA"]["decisionMode"])
    controlData = {
        "goAhead": goAhead,
        "direction": "",
        "sensor": {
            "ultrasonic": {
                "left": 0,
                "right": 0,
                "front": 0
            }
        }
    }

    while goAhead:
        # read sensors and process here
        controlData["sensor"]["ultrasonic"]["right"] = ultrasonicSensor.getValue("right")
        controlData["sensor"]["ultrasonic"]["left"] = ultrasonicSensor.getValue("left")
        controlData["sensor"]["ultrasonic"]["front"] = ultrasonicSensor.getValue("left")

        # very simple logic for PoC -NOTE-remove/reform it after testing
        controlData["direction"] = dDecisions.decide(controlData["sensor"])
        log.info(controlData['sensor']['ultrasonic'])
        log.info("Decision : %s", controlData["direction"])

        time.sleep(2)


# use this for pre-checking for any conditions like communcation, camera, sensors, etc
def initChecks():
    return True

def startMedha():
    # check for SIGNALS
    signalhandler = signalHandler.signalHandler()

    # initialize on exit actions
    atexit.register(ec.exitChecks().atExitCheck1)
    basicChecksThread = threading.Thread(target=startBackgroundTasks, args=(), daemon=True).start()

    # wait for certain initial criteria to become True
    while not initChecks(): time.sleep(1)
    startAutonomy(goAhead=True);

if __name__ == '__main__':
    startMedha()
