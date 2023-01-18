import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r1=randomLowercase(8)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login.cgi?set_language=CN"
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	body=f'user=admin&password=admin&selectLanguage=CN&Submit=%E7%99%BB%E9%99%86'
	response=requests.post(url, body,headers=headers,verify=False,timeout=5)
	if "function init(){window.open('index.htm" in response.text:
		s0=True
	else:
		s0=False
	if s0:
		return True
	else:
		return False
