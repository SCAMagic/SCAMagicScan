import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url = baseurl
	response = requests.get(url=url,verify=False,timeout=5)
	if 'tongda' in response.text:
		url = baseurl + "mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0"
		headers = {
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
			}
		response = requests.get(url=url,headers=headers,verify=False,timeout=5)  #verify=False为忽略CA证书
		if "RELOGIN" in response.text and response.status_code == 200:  #如果页面显示RELOGIN且网站状态码为200
			return True
		elif response.text == "" and response.status_code == 200:  #如果页面空白且状态码为200
			return True
		else:
			return False
	else:
		return False
