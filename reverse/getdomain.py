import requests,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_domain():
	url='https://log.xn--9tr.com/new_gen'
	headers={'Content-type': 'application/x-www-form-urlencoded'}
	body='domain=dns.1433.eu.org.'
	try:
		r=requests.post(url,body,headers=headers,timeout=5,verify=False)
		domain=r.json()['domain']
		token=r.json()['token']
	except:
		domain=''
		token=''
		print("[!!!]	获取dnslog失败")
	return (domain,token)
