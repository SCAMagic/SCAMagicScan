import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"signin"
	body="username=apollo&password=admin&login-submit=%E7%99%BB%E5%BD%95"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList=response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302:
				try:
					cookie=response.headers['Set-Cookie']
				except:
					cookie=''
				f_list.append(1)
		if len(f_list)>0:
			r1=True
		else:
			cookie=''
			r1=False
	else:
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"user"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Cookie": cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "\"userId\":\"apollo\"" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r2=True
		else:
			r2=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "\"userId\":\"apollo\"" in response.text:
			r2=True
		else:
			r2=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"permissions/root"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Cookie": cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "\"hasPermission\":true" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r3=True
		else:
			r3=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "\"hasPermission\":true" in response.text:
			r3=True
		else:
			r3=False
	if r1 and r2 and r3:
		return True
	else:
		return False
