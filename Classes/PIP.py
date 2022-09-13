import os, sys
import subprocess
class PIP():
	def __init__(self, _):
		self._ = _
		self.module = _.args[0]
		self.Main()

	def Main(self):
		self._.Install_Module(self.module)
