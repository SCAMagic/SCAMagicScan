import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/whoami"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 401:
		r0=True
	else:
		r0=False
	url=baseurl+"api/whoami"
	headers={'Authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q='}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "\"name\":\"guest\"" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
