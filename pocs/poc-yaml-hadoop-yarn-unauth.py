import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"ws/v1/cluster/info"
	headers={'Content-Type': 'application/json'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "resourceManagerVersionBuiltOn" in response.text and "hadoopVersion" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "resourceManagerVersionBuiltOn" in response.text and "hadoopVersion" in response.text:
			r0=True
		else:
			r0=False
	if r0:
		return True
	else:
		return False
