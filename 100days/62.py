#!/usr/bin/python
# -*- coding: UTF-8 -*-

#爬取知乎hot话题-2019/05/28
from urlparse import urljoin

import re
import requests

def main():
    headers = {'user-agent':'Baiduspider',
               'cookie':'_zap=98c40a42-ba4b-431f-af1a-96413594b92b; d_c0="AKAhaqKooQ2PTqCm6OaFWbwJKiq9bP92lvY=|1526967033"; _xsrf=0ec2d661-6b11-4ffa-bab9-af0f9ef6b596; l_n_c=1; l_cap_id="MDdlYzVjOGQ0NDBlNDNmYjgxMDFiM2UxMTYyYzlmM2Y=|1559023698|8a4e0c8a6bdb10b384ab18f069387bec597e3dc6"; r_cap_id="NjRiNmZhNjU5MjA5NGU0NzgwYzEzMGRhZWFhMzdhMjM=|1559023698|0cae682d5b66d34aefff9906a651e942d3874cb5"; cap_id="YjQ3MTUxMDhiMDNiNDVjMGJmNDcwY2IzYTI5NGM5OWM=|1559023698|382755d70baa217cae15c38f848c444fcc5d0884"; n_c=1; capsion_ticket="2|1:0|10:1559025080|14:capsion_ticket|44:YWE2MTI3ZGJmYWJmNDQ0M2I5YjY0OWU5ODc1YTQ4Nzk=|1cf522b0d88ae66182b59c245e04d0d661ba8209258284f4f07f9f8b95aa1d8d"; z_c0="2|1:0|10:1559025099|4:z_c0|92:Mi4xRkhRY0FBQUFBQUFBb0NGcW9xaWhEU1lBQUFCZ0FsVk55eVBhWFFBb19abUZXMXRhMFlNTGlBMDFKVDNhN3Fpbjh3|3769cd1456316d629978825346d675166abeff0a9603a64f3d9a26ed3affa604"; q_c1=bf9dc319ee5e464d8db89d962cbd5c4b|1559025105000|1525850898000; tst=h; __utmc=51854390; __utmv=51854390.100--|2=registration_date=20131018=1^3=entry_date=20131018=1; __utma=51854390.1130677542.1559025463.1559025463.1559027349.2; __utmb=51854390.0.10.1559027349; __utmz=51854390.1559027349.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7'          
    }
    proxies = {
        'http':'http://122.114.31.177:808'
    }
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'hot')
    resp = requests.get(seed_url,
                        headers=headers,
                        proxies=proxies)
    html = resp.text
    match_obj = re.compile(r'<h2 class="HotItem-title">.*?</h2>', re.S)
    results = re.findall(match_obj, html)
    for item in results:
        match_title = r'<h2 class="HotItem-title">(.*?)</h2>'
        title = re.findall(match_title, item)[0]
        print title

if __name__ == '__main__':
    main()
