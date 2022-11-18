import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	r=0
	payload={
	'path01':{'urlpath':'mail-server','body':'page.admin.mailServer','res':'Use SSL/TLS if available'},
	'path02':{'urlpath':'db','body':'page.db','res':'Database Type'},
	'path03':{'urlpath':'db/edit','body':'page.admin.editDbConfig','res':'Migrate Database'},
	'path04':{'urlpath':'license','body':'page.admin.license','res':'License Settings'},
	'path05':{'urlpath':'logging','body':'layout.admin','res':'Logging and Profiling'},
	'path06':{'urlpath':'server-settings','body':'page.admin.server','res':'Server settings'},
	'path07':{'urlpath':'authentication','body':'page.admin.authentication','res':'Authentication'},
	'path08':{'urlpath':'avatars','body':'layout.admin','res':'Avatars'},
	}
	key_list=list(payload.keys())
	for key in key_list:
		try:
			urlpath=payload[key]['urlpath']
			body=payload[key]['body']
			res=payload[key]['res']
			url=baseurl+f"admin%20/{urlpath}"
			headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
			response=requests.get(url,headers=headers,timeout=5,verify=False)
			if response.status_code == 200 and res in response.text and ("download/contextbatch/js/bitbucket." + body in response.text or "download/contextbatch/css/bitbucket." + body in response.text):
				r+=1
		except:
			pass
	if r!=0:
		return True
	else:
		return False
