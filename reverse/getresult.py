import requests,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_result(domain,token):
	if 'dnslog.cn' in domain:
		flag=dnslog1(domain,token)
	else:
		flag=dnslog2(domain,token)
	return flag
def dnslog1(domain,cookie):
	url='http://dnslog.cn/getrecords.php?t=0.0701635123201233'
	headers={
	"Cookie":cookie
	}
	try:
		r=requests.get(url,headers=headers,timeout=5,verify=False)
		if '[]'!=r.text:
			return True
		else:
			return False
	except:
		print("[!!!]	dnslog.cn刷新dnslog失败")
		return False
def dnslog2(domain,token):
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
		print("[!!!]	dns.1433.eu.org刷新dnslog失败")
		return False
