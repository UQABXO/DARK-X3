import json
class Geo():
	def __init__(self,_):
		self._ = _
		self.Main()

	def Main(self):
		data = json.loads(self._.Request('http://ip-api.com/json/'))
		result = "%F0%9F%8C%8E Geo Location : \n"
		result += "%E2%9D%96 IP : " + data['query'] + "\n";
		result += "%E2%9D%96 Country : " + data['country'] + "\n";
		result += "%E2%9D%96 City : " + data['city'] + "\n";
		result += "%E2%9D%96 Region Name : " + data['regionName'] + "\n";
		result += "%E2%9D%96 Country Code : " + data['countryCode'] + "\n";
		result += "%E2%9D%96 Time Zone : " + data['timezone'] + "\n";
		result += "%E2%9D%96 MAP : http://extreme-ip-lookup.com/" + data['query'];
		self._.Send_Message(result)
