import re
import requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
user=randomLowercase(8)
def scan(baseurl):
	url=baseurl+'ibm/console/login.do'
	headers={"Content-Type": "application/x-www-form-urlencoded"}
	body=f'username={user}&submit=Log+in'
	response = requests.post(url,body,headers=headers,timeout=5,verify=False)
	if "/ibm/console/secure/isclite/tiles/bannerframe.jsp" in response.text:
		return True
	else:
		return False