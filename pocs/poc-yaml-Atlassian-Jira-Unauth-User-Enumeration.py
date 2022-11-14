import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"secure/QueryComponentRendererValue!Default.jspa?assignee=user:admin"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "rel=" in response.text and "assignee" in response.text and str("application/json" in response.headers["Content-Type"]):
				f_list.append(1)
		if len(f_list)==1:
			r10=True
		else:
			r10=False
	else:
		if response.status_code == 200 and "rel=" in response.text and "assignee" in response.text and str("application/json" in response.headers["Content-Type"]):
			r10=True
		else:
			r10=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"jira/secure/QueryComponentRendererValue!Default.jspa?assignee=user:admin"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "rel=" in response.text and "Assignee" in response.text and str("application/json" in response.headers["Content-Type"]):
				f_list.append(1)
		if len(f_list)==1:
			r20=True
		else:
			r20=False
	else:
		if response.status_code == 200 and "rel=" in response.text and "Assignee" in response.text and str("application/json" in response.headers["Content-Type"]):
			r20=True
		else:
			r20=False
	if r10 or r20:
		return True
	else:
		return False
