import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/tokens"
	body="username=guacadmin&password=guacadmin"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "\"userID\":\"guacadmin\"" in response.text and "\"authToken\"" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
