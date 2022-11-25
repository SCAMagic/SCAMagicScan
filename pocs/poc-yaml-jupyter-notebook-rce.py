import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/terminals"
	headers={'cookie': '_xsrf=2|7a4faae0|819f5adf7edaef5e74502c9d0c75a604|1653492335', 'X-XSRFToken': '2|7a4faae0|819f5adf7edaef5e74502c9d0c75a604|1653492335'}
	body=''
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if "name" in response.text and "last_activity" in response.text and response.status_code == 200:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
