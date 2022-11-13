import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"plugin.php?id=wechat:wechat&ac=wxregister"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and "set-cookie" in response.headers and "auth" in response.headers["set-cookie"] and "location" in response.headers and "wsq.discuz.com" in response.headers["location"]:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "set-cookie" in response.headers and "auth" in response.headers["set-cookie"] and "location" in response.headers and "wsq.discuz.com" in response.headers["location"]:
			r0=True
		else:
			r0=False
	if r0:
		return True
	else:
		return False
