import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login/"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		l0=True
	else:
		l0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
		try:
			cookie=response.headers['Set-Cookie']
		except:
			cookie=''
		try:
			token=re.findall("<input id=\"csrf_token\" name=\"csrf_token\" type=\"hidden\" value=\"(.+?)\"",response.text)[0]
		except:
			token=''
	else:
		baseurl=baseurl+"/"
		token=''
		cookie=''
	url=baseurl+"login/"
	body=f"username=airflow&password=airlow&_csrf_token={token}"
	headers={'Content-Type': 'application/x-www-form-urlencoded','Cookie':cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "login" in response.headers['Location']:
				f_list.append(1)
		if len(f_list)!=0:
			r0=True
		else:
			r0=False
	else:
		r0=False
	url=baseurl+"login/"
	body=f"username=airflow&password=airflow&_csrf_token={token}"
	headers={'Content-Type': 'application/x-www-form-urlencoded','Cookie':cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "login" not in response.headers['Location']:
				f_list.append(1)
		if len(f_list)!=0:
			r1=True
		else:
			r1=False
	else:
		if response.status_code==200 and '<title>Airflow - Login</title>' in response.text:
			r1=True
		else:
			r1=False
	url=baseurl+"admin/airflow/login"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	body=f"username=airflow&password=arflow&_csrf_token={token}"
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 404:
		r2=True
	else:
		r2=False
	url=baseurl+"admin/airflow/login"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	body=f"username=airflow&password=airflow&_csrf_token={token}"
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code != 404:
		r3=True
	else:
		r3=False
	if l0 and ((r0 and r1) or (r2 and r3)):
		return True
	else:
		return False
