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
r1=randomLowercase(5)
def scan(baseurl):
	url=baseurl+"/api/v1/authentication/connection-token/"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 401 and "application/json" in response.headers["Content-Type"] and "not_authenticated" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			authentication0=True
		else:
			authentication0=False
	else:
		if response.status_code == 401 and "application/json" in response.headers["Content-Type"] and "not_authenticated" in response.text:
			authentication0=True
		else:
			authentication0=False
	url=baseurl+"/api/v1/authentication/connection-token/?user-only="+r1+""
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 404 and "application/json" in response.headers["Content-Type"] and "\"\"" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			authentication1=True
		else:
			authentication1=False
	else:
		if response.status_code == 404 and "application/json" in response.headers["Content-Type"] and "\"\"" in response.text:
			authentication1=True
		else:
			authentication1=False
	url=baseurl+"/api/v1/users/connection-token/"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 401 and "application/json" in response.headers["Content-Type"] and "not_authenticated" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			users0=True
		else:
			users0=False
	else:
		if response.status_code == 401 and "application/json" in response.headers["Content-Type"] and "not_authenticated" in response.text:
			users0=True
		else:
			users0=False
	url=baseurl+"/api/v1/users/connection-token/?user-only="+r1+""
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 404 and "application/json" in response.headers["Content-Type"] and "\"\"" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			users1=True
		else:
			users1=False
	else:
		if response.status_code == 404 and "application/json" in response.headers["Content-Type"] and "\"\"" in response.text:
			users1=True
		else:
			users1=False
	if users0 and users1 or authentication0 and authentication1:
		return True
	else:
		return False
