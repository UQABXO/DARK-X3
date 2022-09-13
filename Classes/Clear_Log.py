import os, sys
class Clear_Log():
	def __init__(self, _):
		self._ = _
		self.Main()

	def Main(self):
		filename = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\Keylogger.txt"
		if os.path.exists(filename):
			os.remove(filename)
			self._.Send_Message("%E2%9C%94%EF%B8%8F Keylogger Log Deleted")
		else:
			self._.Send_Message("%E2%9C%96%EF%B8%8F Log File Not Exists")
