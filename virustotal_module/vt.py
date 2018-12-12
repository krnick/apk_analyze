import requests

class VT():
	api_key = ""
	hash_code = ""	

	def __init__(self,api_key,hash_code):
		self.api_key = api_key
		self.hash_code = hash_code


	def getVT_result(self):
		params = {'apikey': self.api_key, 'resource':self.hash_code}
		headers = {
		"Accept-Encoding": "gzip, deflate",
		"User-Agent" : "gzip,  My Python requests library example client or username"
		}
		response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
		params=params, headers=headers)
		json_response = response.json()
		print(str(json_response['positives'])+"/"+str(json_response['total']))




