import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login.cgi"
	body="user=admin&password1=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81&password=123456&Submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
	"Content-Type": "application/x-www-form-urlencoded"
	}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "ac_userid=admin,ac_passwd=" in response.headers["Set-Cookie"] and "window.open('index.htm?_" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "ac_userid=admin,ac_passwd=" in response.headers["Set-Cookie"] and "window.open('index.htm?_" in response.text:
			r0=True
		else:
			r0=False
	if r0:
		return True
	else:
		return False
