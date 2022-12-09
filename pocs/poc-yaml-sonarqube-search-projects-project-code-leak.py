import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/components/search_projects"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if "{\"paging\":{\"pageIndex\":1,\"pageSize\"" in response.text and "\"visibility\":\"public\"" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
