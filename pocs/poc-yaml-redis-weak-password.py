import socket,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getdomain(url):
	# if '/' in url:
	url = url.replace('http://', '').replace('https://', '')
	url = url + '/'
	url = url.split('/')[0]
	return url
def scan(baseurl):
	domain=getdomain(baseurl)
	ip=domain.split(':')[0]
	port=int(domain.split(':')[1])
	socket.setdefaulttimeout(5)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(bytes("INFO\r\n", 'UTF-8'))
	result = s.recv(1024).decode()
	s.close()
	if "Authentication" in result:
		flag=[]
		pass_list=['redis','root','oracle','password','p@ssw0rd','abc123!','123456','admin','abc123','root123','admin123']
		for passwd in pass_list:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, int(port)))
			s.send(bytes("AUTH %s\r\n" %(passwd),'UTF-8'))
			result = s.recv(1024).decode()
			if 'OK' in result:
				flag.append(1)
				break
		if len(flag)>0:
			return True
		else:
			return False
	else:
		return False