from implModules import actuateMotors

class POC1():
    def __init__(self):
        self.acM = actuateMotors.setMotors()

    def setMotion(self, motionName):
        self.acM.setMotion(motionName)

    def cleanup(self):
        self.acM.cleanup()
