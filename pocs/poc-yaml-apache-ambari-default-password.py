import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"api/v1/users/admin?fields=*,privileges/PrivilegeInfo/cluster_name,privileges/PrivilegeInfo/permission_name"
	headers={'Authorization': 'Basic YWRtaW46YWRtaW4='}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "PrivilegeInfo" in response.text and "AMBARI.ADMINISTRATOR" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
