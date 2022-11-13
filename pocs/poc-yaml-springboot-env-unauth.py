import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"env"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "java.version" in response.text and "os.arch" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			spring10=True
		else:
			spring10=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "java.version" in response.text and "os.arch" in response.text:
			spring10=True
		else:
			spring10=False
	url=baseurl+"actuator/env"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "java.version" in response.text and "os.arch" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			spring20=True
		else:
			spring20=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "java.version" in response.text and "os.arch" in response.text:
			spring20=True
		else:
			spring20=False
	if spring10 or spring20:
		return True
	else:
		return False
