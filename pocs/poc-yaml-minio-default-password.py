import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"minio/webrpc"
	body='{"id":1,"jsonrpc":"2.0","params":{"username":"minioadmin","password":"minioadmin"},"method":"Web.Login"}'
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0','Content-Type': 'application/json'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "uiVersion" in response.text and "token" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			poc10=True
		else:
			poc10=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "uiVersion" in response.text and "token" in response.text:
			poc10=True
		else:
			poc10=False

	url=baseurl+"minio/webrpc"
	body='{"id":1,"jsonrpc":"2.0","params":{"username":"minioadmin","password":"minioadmin"},"method":"web.Login"}'
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0','Content-Type': 'application/json'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "uiVersion" in response.text and "token" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			poc20=True
		else:
			poc20=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "uiVersion" in response.text and "token" in response.text:
			poc20=True
		else:
			poc20=False
	if poc10 or poc20:
		return True
	else:
		return False
