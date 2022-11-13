import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
name=randomInt(10000000, 99999999)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+""+str(name)+".php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code != 200:
		html0=True
	else:
		html0=False
	url=baseurl+"index.html"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "nginx" in response.headers["Server"]:
				f_list.append(1)
		if len(f_list)==1:
			html1=True
		else:
			html1=False
	else:
		if response.status_code == 200 and "nginx" in response.headers["Server"]:
			html1=True
		else:
			html1=False
	url=baseurl+"index.html/.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "nginx" in response.headers["Server"]:
				f_list.append(1)
		if len(f_list)==1:
			html2=True
		else:
			html2=False
	else:
		if response.status_code == 200 and "nginx" in response.headers["Server"]:
			html2=True
		else:
			html2=False
	url=baseurl+"index.html/.xxx"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code != 200:
		html3=True
	else:
		html3=False
	url=baseurl+""+str(name)+".php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code != 200:
		php0=True
	else:
		php0=False
	url=baseurl+"index.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "nginx" in response.headers["Server"]:
				f_list.append(1)
		if len(f_list)==1:
			php1=True
		else:
			php1=False
	else:
		if response.status_code == 200 and "nginx" in response.headers["Server"]:
			php1=True
		else:
			php1=False
	url=baseurl+"index.php/.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "nginx" in response.headers["Server"]:
				f_list.append(1)
		if len(f_list)==1:
			php2=True
		else:
			php2=False
	else:
		if response.status_code == 200 and "nginx" in response.headers["Server"]:
			php2=True
		else:
			php2=False
	url=baseurl+"index.php/.xxx"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code != 200:
		php3=True
	else:
		php3=False
	if html0 and html1 and html2 and html3 or php0 and php1 and php2 and php3:
		return True
	else:
		return False
