#-*-coding:utf-8-*-
import socket
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
	try:
		socket.setdefaulttimeout(5)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send(bytes('envi', 'UTF-8'))
		data = s.recv(1024).decode()
		s.close()
		if 'Environment' in data:
			return True
		else:
			return False	
	except:
		return False



