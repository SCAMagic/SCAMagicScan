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
rand=randomLowercase(6)
def scan(baseurl):
	url=baseurl+"uapws/service"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and response.text.startswith("<html><head><meta http-equiv=\"content-type\" content=\"text/html;") and re.search("{http://.*?}IMetaWebService4BqCloudPort",response.text):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
