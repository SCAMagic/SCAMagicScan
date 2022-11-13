import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/proxy/tcp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 401 and "Unauthorized" in response.text:
		defaultpassword0=True
	else:
		defaultpassword0=False
	url=baseurl+"api/proxy/tcp"
	headers={'Authorization': 'Basic YWRtaW46YWRtaW4='}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "text/plain" in response.headers["Content-Type"] and "proxies" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			defaultpassword1=True
		else:
			defaultpassword1=False
	else:
		if response.status_code == 200 and "text/plain" in response.headers["Content-Type"] and "proxies" in response.text:
			defaultpassword1=True
		else:
			defaultpassword1=False
	url=baseurl+"api/proxy/tcp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "text/plain" in response.headers["Content-Type"] and "proxies" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			unauth0=True
		else:
			unauth0=False
	else:
		if response.status_code == 200 and "text/plain" in response.headers["Content-Type"] and "proxies" in response.text:
			unauth0=True
		else:
			unauth0=False
	if unauth0 or defaultpassword0 and defaultpassword1:
		return True
	else:
		return False
