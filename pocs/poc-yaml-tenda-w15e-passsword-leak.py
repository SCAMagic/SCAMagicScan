import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"cgi-bin/DownloadCfg/RouterCfm.cfg"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if "wl2g.ssid2.wmm" in response.text and "wl5g.ssid0.wmm" in response.text and "wl2g.ssid3.wmm=" in response.text and "wl5g.ssid1.wmm=" in response.text and "wl5g.ssid2.wmm=" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
