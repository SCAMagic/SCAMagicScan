import requests,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_domain():
	url='http://dnslog.cn/getdomain.php?t=0.9427873201991249'
	headers={'Referer': 'http://dnslog.cn/'}
	try:
		r=requests.get(url,headers=headers,timeout=5,verify=False)
		domain=r.text
		token=r.headers['Set-Cookie']
		result=(domain,token)
	except:
		result=dnslog2()
	return result
def dnslog2():
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
# print(get_domain())
