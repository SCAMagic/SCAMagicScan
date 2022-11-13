import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl
	headers={'Authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q='}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<title>Dubbo Admin</title>" in response.text and ": guest', '/logout'" in response.text and "/sysinfo/versions" in response.text:
		guest0=True
	else:
		guest0=False
	url=baseurl
	headers={'Authorization': 'Basic cm9vdDpyb290'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<title>Dubbo Admin</title>" in response.text and ": root', '/logout'" in response.text and "/sysinfo/versions" in response.text:
		root0=True
	else:
		root0=False
	if root0 or guest0:
		return True
	else:
		return False
