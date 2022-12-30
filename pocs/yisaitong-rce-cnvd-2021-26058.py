#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,re,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def scan(baseurl):
    url = '{}solr/admin/cores'.format(baseurl)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }
    r = requests.get(url, headers=headers, verify=False, timeout=10)
    final_result = r.text
    if r.status_code == 200:
        result = re.search(r'<str name="name">([\s\S]*?)</str><str name="instanceDir">', final_result, re.I)
        if result:
            return True
        else:
            return False
    else:
        return False

