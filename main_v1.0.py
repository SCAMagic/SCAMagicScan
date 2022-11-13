import socket
import threading
from threading import Thread
import requests,re,argparse,sys,os
import requests.packages.urllib3
import subprocess
from urllib.request import urlopen
from hashlib import md5
import base64
import time
from urllib import parse
# import colorama
 
# colorama.init(autoreset=True)

urllist=[]
poclist=[]
total_list=[]
urlSepList=[]
# num=0
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', type=str,help=' url文件路径')
	parser.add_argument('-u', '--url', type=str, help=' 主机地址 ')
	parser.add_argument('-p', '--poc', type=str, help=' poc名,多个以逗号隔开,支持*号模糊匹配')
	parser.add_argument('-t', '--thread', type=int, help=' 线程数量(默认1500,数量越低，准确率越高) ')
	args = parser.parse_args()

	file = args.file
	url   = args.url
	poc = args.poc
	max_t_num=args.thread
	if len(sys.argv)<2:
		print("Usage: python3 MagicScan.py -h 查看帮助")
	else:
		SCAMagicscan(file,url,poc,max_t_num)
def SCAMagicscan(file,url,poc,max_t_num):
	if file !=None and url ==None:
		url_app(file)
	elif file ==None and url !=None:
		urllist.append(url)
	elif file ==None and url ==None:
		print('缺少file参数或url参数！')
		sys.exit(0)
	else:
		print('file参数和url参数不能同时存在！')
		sys.exit(0)
	if poc!=None:
		import_poc(poc)
	else:
		l=os.listdir('pocs')
		l=[i for i in l if '.py' in i]
		for p in l:
			p='pocs/'+p.replace('.py','')
			poclist.append(p)
	if max_t_num==None:
		max_t_num=1500
	startscan(max_t_num)
def url_app(file):
	with open(file,'r',encoding='utf-8') as f:
		for c in f.readlines():
			c=c.strip('\n')
			urllist.append(c)
def import_poc(poc):
	l=poc.split(',')
	for p in l:
		if '*' in p:
			num=0
			p=p.replace('*','.*')
			for ps in os.listdir('pocs'):
				pl=[]
				pl.append(ps)
				if re.findall(p,ps)==pl:
					poclist.append('pocs/'+ps.replace('.py',''))
					num+=1
			if num==0:
				print(p+'无效poc')
				sys.exit(0)
		else:
				if p+'.py' in os.listdir('pocs'):
					p='pocs/'+p
					poclist.append(p)
				else:
					print(p+'无效poc')
					sys.exit(0)
def startscan(max_t_num):
	for i in urllist:
		for j in poclist:
			total_list.append((i,j))
	total=len(total_list)
	if total<max_t_num:
		threading_num=total
	else:
		threading_num=max_t_num
	multithreading(threading_num,total)

					
#分离文件名 给每个线程分一个
def separateName(threadCount):
	for i in range(0,len(total_list),int(len(total_list)/threadCount)):
		urlSepList.append(total_list[i:i+int(len(total_list)/threadCount)])
# #多线程函数
def multithreading(threadCount,total):
	separateName(threadCount)#先分离
	for i in range(0,len(urlSepList)):
		t=Thread(target=bp,args=(urlSepList[i],total))
		t.start()
	t.join()

def bp(target_list,total):
	sys.path.insert(0,'pocs')
	# global num
	for target in target_list:
		# num+=1
		# try:
		url=target[0]
		poc=target[1]
		if 'http' not in url:
			url='http://'+url
		pocname=poc.split('/')[1]
		# print(pocname)
		# from pocname import pocname
		try:
			module = __import__(pocname)
			flag=module.scan(url)
			if flag==True:
				print(f'[+++]	{url}	{pocname}')
				ff=open('vuln.txt','a',encoding='utf-8')
				ff.write(f'{url}	{pocname}\n')
				ff.close()
			else:
				print(f'[---]	{url}	{pocname}')
		except Exception as e:
			if 'HTTPConnectionPool' in str(e) or 'HTTPSConnectionPool' in str(e) or 'Connection aborted' in str(e):
				print(f'[!!!]  {url}   {pocname}   连接失败')
			else:
				print(f'[!!!]	{url}   {pocname}	{e}')
		# print(str(num)+'/'+str(total))
		# mystr1 = "进度：" + str(num) + "/" + str(total)
		# mystr2 ='百分比: {:.3f}%'.format(num/total*100)
		# mystr=mystr1+'  '+mystr2
		# print(mystr,end = ""),
		# print("\b" * (len(mystr)*2),end = "",flush=True)
def logo():
    print('''
   _____   _____            __  __                _         _____                    \r
  / ____| / ____|    /\    |  \/  |              (_)       / ____|                   \r
 | (___  | |        /  \   | \  / |  __ _   __ _  _   ___ | (___    ___  __ _  _ __  \r
  \___ \ | |       / /\ \  | |\/| | / _` | / _` || | / __| \___ \  / __|/ _` || '_ \ \r
  ____) || |____  / ____ \ | |  | || (_| || (_| || || (__  ____) || (__| (_| || | | |\r
 |_____/  \_____|/_/    \_\|_|  |_| \__,_| \__, ||_| \___||_____/  \___|\__,_||_| |_|\r
                                            __/ |                                    \r
                                           |___/                                     \r
                                                       ---by SCAMagic\r
        ''')


if __name__ == '__main__':
	logo()
	main()