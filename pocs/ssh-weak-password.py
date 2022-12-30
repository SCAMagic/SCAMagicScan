import paramiko,re
import argparse
def scan(baseurl):
	total=[]
	flag=[]
	user_list=['root','admin','test','system','web']
	pass_list=['root','123456','1234','test','admin','root123']
	# user_list=['root']
	# pass_list=['DsBzaq1ZAQ!']
	for u in user_list:
		for p in pass_list:
			total.append((u,p))
	for t in total:
		user=t[0]
		passw=t[1]
		host=re.findall('http://(.+?):',baseurl)[0]
		port=int(baseurl.split(':')[2].split('/')[0])
		print(user,passw)
		try:
			# 使用 paramiko.SSHClient 创建 ssh 对象
			ssh = paramiko.SSHClient()
			# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面，接受对方的公钥证书
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			# 登录 ssh，连接失败则抛出 异常 跳转到 except ，成功则继续执行
			ssh.connect(hostname=host,port=port,username=user,password=passw,timeout=5)
			ssh.close()
			flag.append(1)
			break
			# 打印出成功登录的 用户名 和 密码
			# 把 flag 置为 1
	 		
		except:
			pass
		finally:
			ssh.close()
	if len(flag)>0:
		return True
	else:
		return False