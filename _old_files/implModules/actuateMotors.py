import os
import json
import RPi.GPIO as GPIO
import logging

# init log module
log = logging.getLogger(__name__)

class setMotors:
    motionTable = {
        "stop": {
            "motorL": { "a": GPIO.LOW, "b": GPIO.LOW },
            "motorR": { "a": GPIO.LOW, "b": GPIO.LOW }
        },
        "front": {
            "motorL": { "a": GPIO.LOW, "b": GPIO.HIGH },
            "motorR": { "a": GPIO.LOW, "b": GPIO.HIGH }
        },
        "back": {
            "motorL": { "a": GPIO.HIGH, "b": GPIO.LOW },
            "motorR": { "a": GPIO.HIGH, "b": GPIO.LOW }
        },
        "right": {
            "motorL": { "a": GPIO.LOW, "b": GPIO.HIGH },
            "motorR": { "a": GPIO.HIGH, "b": GPIO.LOW }
        },
        "left": {
            "motorL": { "a": GPIO.HIGH, "b": GPIO.LOW },
            "motorR": { "a": GPIO.LOW, "b": GPIO.HIGH }
        }
    }

    def __init__(self):

        GPIO.cleanup()
        PINS_FILE = "pins.json"
        with open(PINS_FILE) as pins:
            self.pins = json.load(pins)
        GPIO.setmode( GPIO.BOARD )
        GPIO.setup( self.pins["motorL"]["a"], GPIO.OUT )
        GPIO.setup( self.pins["motorL"]["b"], GPIO.OUT )
        GPIO.setup( self.pins["motorR"]["a"], GPIO.OUT )
        GPIO.setup( self.pins["motorR"]["b"], GPIO.OUT )
        log.debug("initializing actuateMotors")

    def cleanup(self):
        log.info("cleaning GPIO")
        GPIO.cleanup()

    def setMotion(self, motionName):
        if motionName not in self.motionTable:
            log.error("unknown motionName: %s", motionName)
        else:
            log.info("setting motion to: %s", motionName)
            motionSet = self.motionTable[motionName]
            for motor in motionSet:
                for pin in motionSet[motor]:
                    GPIO.output( self.pins[motor][pin], motionSet[motor][pin] )
