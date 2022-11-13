import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/v1/GetSrc"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "json" in response.headers["Content-Type"] and "H5_AUTO" in response.text and "strUser" in response.text and "strPasswd" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			h5s1=True
		else:
			h5s1=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "H5_AUTO" in response.text and "strUser" in response.text and "strPasswd" in response.text:
			h5s1=True
		else:
			h5s1=False
	url=baseurl+"api/v1/GetDevice"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "json" in response.headers["Content-Type"] and "H5_DEV" in response.text and "strUser" in response.text and "strPasswd" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			h5s2=True
		else:
			h5s2=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "H5_DEV" in response.text and "strUser" in response.text and "strPasswd" in response.text:
			h5s2=True
		else:
			h5s2=False
	if h5s1 or h5s2:
		return True
	else:
		return False
