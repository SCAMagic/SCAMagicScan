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
r11=randomLowercase(32)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r22=randomLowercase(32)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r3=randomLowercase(32)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"v2/keys/"+r11+"?dir=true"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	body=''
	response=requests.put(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 201:
		r0=True
	else:
		r0=False
	url=baseurl+"v2/keys/"+r11+"/"+r22+"?prevExist=false"
	body="value="+r3+""
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.put(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 201:
		r1=True
	else:
		r1=False
	url=baseurl+"v2/keys/"+r11+"/"+r22+"?quorum=false&recursive=false&sorted=false"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and r3 in response.text:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
