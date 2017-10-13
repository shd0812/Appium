import ConfigParser
import os

top_Dir=os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(top_Dir,'config.ini')

class ReadConfig:
	def __init__(self):
		self.cf=ConfigParser.ConfigParser()
		self.cf.read(config_path)
	
	def getVaule(self,name):
		vaule =self.cf.get('DriverConfig',name)
		return vaule
	
	def getOther(self,name):
		vaule=self.cf.get('other',name)
		return vaule

