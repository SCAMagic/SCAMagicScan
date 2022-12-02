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
	if "redis_version" in result:
		return True
	else:
		return False