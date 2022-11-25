import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"request_para.cgi?parameter=wifi_info"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("\"wl_enable_2g\":\"[0-9]\",\"wl_enable_5g\":\"[0-9]*",response.text):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
