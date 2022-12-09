import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		session1=requests.Session()
		url=baseurl+"general/login_code.php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=session1.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "code_uid" in response.text:
			r0=True
			try:
				codeuid=re.findall("\"code_uid\":\"((.*?))\"",response.text)[0]
			except:
				codeuid=''
		else:
			codeuid=''
			r0=False
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"logincheck_code.php"
		body=f"CODEUID={codeuid}&UID=1"
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=session1.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200:
			r1=True
		else:
			r1=False
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"general/index.php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=session1.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "/inc/js_lang.php" in response.text and "/static/js/intro/show_guide.css" in response.text:
			r2=True
		else:
			r2=False
	except:
		r1=False
		r2=False
		r0=False
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		session2=requests.Session()
		url=baseurl+"ispirit/login_code.php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=session2.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "codeuid" in response.text:
			r3=True
			try:
				codeuid=re.findall("\"code_uid\":\"((.*?))\"",response.text)[0]
			except:
				codeuid=''
		else:
			codeuid=''
			r3=False
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"general/login_code_scan.php"
		body=f"codeuid={codeuid}&uid=1&source=pc&type=confirm&username=admin"
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=session2.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200:
			r4=True
		else:
			r4=False
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+f"ispirit/login_code_check.php?codeuid={codeuid}"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=session2.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "PHPSESSID=" in response.headers["Set-Cookie"]:
			r5=True
		else:
			r5=False
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"general/index.php"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=session2.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "/inc/js_lang.php" in response.text and "/static/js/intro/show_guide.css" in response.text:
			r6=True
		else:
			r6=False
	except:
		r3=False
		r4=False
		r5=False
		r6=False
	if (r0 and r1 and r2) or (r3 and r4 and r5 and r6):
		return True
	else:
		return False
