import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+'userportal/Controller?mode=8700&operation=1&datagrid=179&json={"🦞":"test"}'
	headers={'X-Requested-With': 'XMLHttpRequest'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "{\"status\":\"Session Expired\"}" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
