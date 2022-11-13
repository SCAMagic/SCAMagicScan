import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"h2-console"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Welcome to H2" in response.text:
		r0=True
		try:
			token=re.findall("location.href = '(.+?)'",response.text)[0]
		except:
			token=''
	else:
		token=''
		r0=False
	url=baseurl+"h2-console/"+token
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Generic H2" in response.text:
		r1=True
	else:
		r1=False
	url=baseurl
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Welcome to H2" in response.text:
		r2=True
		try:
			token=re.findall("location.href = '(.+?)'",response.text)[0]
		except:
			token=''
	else:
		token=''
		r2=False
	url=baseurl+token
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Generic H2" in response.text:
		r3=True
	else:
		r3=False
	if (r0 and r1) or (r2 and r3):
		return True
	else:
		return False
