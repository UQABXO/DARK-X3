import os
class Close():
	def __init__(self):
		self.Main()

	def Main(self):
		os.system("taskkill /IM python.exe /F")
