import requests
import random
import os
import sys
from urllib.parse import urlparse
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'authorization': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36',
}

def scan(target):
    """
    检测目标v2board是否为v1.6.1漏洞版本
    """
    s=requests.Session()
    path = '/api/v1/admin/config/fetch'
    url = f"{target}{path}".replace('//api','/api')
    r = s.get(url,headers=headers,verify=False)
    if r.status_code == 403 and '\\u9274\\u6743\\u5931\\u8d25'  in r.text:
        return True
    else:
        return False    
      
  

  
