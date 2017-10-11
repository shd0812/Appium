import time
from subprocess import Popen
import os
def startappium():
	
	Popen('D:/Python/Appium/server/startAppium.bat',shell = True)
	#time.sleep(8)

def stopappium():
	Popen(' D:/Python/Appium/server/stopAppium.bat',shell = True)
#stopappium()
#startappium()