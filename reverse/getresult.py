import requests,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_result(domain,token):
	url='https://log.xn--9tr.com/get_results'
	headers={'Content-type': 'application/x-www-form-urlencoded'}
	body='domain='+domain+'&token='+token
	try:
		r=requests.post(url,body,headers=headers,timeout=5,verify=False)
		if 'null' not in r.text:
			return True
		else:
			return False
	except:
		print("[!!!]	刷新dnslog失败")
		return False