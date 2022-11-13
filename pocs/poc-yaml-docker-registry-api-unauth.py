import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"v2/"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "docker-distribution-api-version" in response.headers and "registry/2.0" in response.headers["docker-distribution-api-version"]:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "docker-distribution-api-version" in response.headers and "registry/2.0" in response.headers["docker-distribution-api-version"]:
			r0=True
		else:
			r0=False
	url=baseurl+"v2/_catalog"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "application/json" in response.headers["Content-Type"] and "repositories" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r1=True
		else:
			r1=False
	else:
		if response.status_code == 200 and "application/json" in response.headers["Content-Type"] and "repositories" in response.text:
			r1=True
		else:
			r1=False
	if r0 and r1:
		return True
	else:
		return False
