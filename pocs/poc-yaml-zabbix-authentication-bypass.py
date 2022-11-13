import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	try:
		url = "{}latest.php?ddreset=1".format(baseurl,)
		res = requests.get(url,timeout=5,verify=False)
		res.encoding='utf-8'
		if res.status_code == 200 and "Triggers" in res.text:
			r0=True
		else:
			r0=False
	except:
		r0=False
	try:
		url = "{}zabbix.php?action=problem.view&ddreset=1".format(baseurl,)
		res = requests.get(url,timeout=5,verify=False)
		res.encoding='utf-8'
		if res.status_code == 200 and 'zabbix' in res.text and ('Problems' in res.text or '问题' in res.text):
			r1=True
		else:
			r1=False
	except:
		r1=False
	try:
		url = "{}overview.php?ddreset=1".format(baseurl,)
		res = requests.get(url,timeout=5,verify=False)
		res.encoding='utf-8'
		if res.status_code == 200 and 'zabbix' in res.text and ('Overview' in res.text or '概览' in res.text):
			r2=True
		else:
			r2=False
	except:
		r2=False
	try:
		url = "{}srv_status.php?ddreset=1".format(baseurl,)
		res = requests.get(url,timeout=5,verify=False)
		res.encoding='utf-8'
		if res.status_code == 200 and 'zabbix' in res.text and ('Services' in res.text or '服务' in res.text):
			r3=True
		else:
			r3=False
	except:
		r3=False
	if r0 or r1 or r2 or r3:
		return True
	else:
		return False
