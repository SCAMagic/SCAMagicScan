import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
	if url[-1]=='/':
		url2=url+'v2/api-docs'
	else:
		url2=url+'/v2/api-docs'
	r=requests.get(url2,timeout=5,verify=False)
	if 'swagger' in r.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
