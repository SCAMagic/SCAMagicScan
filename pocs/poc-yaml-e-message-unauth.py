import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"setup/setup-datasource-standard.jsp"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	response.encoding='utf-8'
	if "指定 JDBC 驱动程序和连接属性以连接到ecolog数据库" in response.text and "span class=\"jive-setup-helpicon\" onmouseover=\"domTT_activate(this, event" in response.text and "IgniteRealtime.org" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
