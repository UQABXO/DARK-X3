import sys
import os
class Ask_Admin():
	def __init__(self):
		self.Main()

	def Main(self):
		import win32com.shell.shell as shell
		if sys.argv[-1] != 'asadmin':
			script = os.path.abspath(sys.argv[0])
			params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
			while True:
				try:
					shell.ShellExecuteEx(lpVerb='runas', lpFile="cmd.exe", lpParameters="/c " + sys.executable + " " + params)
					os.system("taskkill /IM python.exe /F")
				except Exception as ex:
					pass
