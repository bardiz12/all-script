#!/usr/bin/env python3
import requests
import sys
import re

if len(sys.argv) <= 1 :
    print("usage : python app.py [URL]")
    exit()

r = requests.get(sys.argv[1])
s = re.findall(r"videoId \= \"(.*?)\";", r.text)
if len(s) < 2:
    print("not found")
    exit()

print("Link : https://youtube.com/watch?v={}".format(s[1]))

python app.py https://zulu.id/video/17-17-6858/tonight-show-season-1/kesibukan-seorang-manohara-sebagai-seorang-aktivis-hewan
Link : https://youtube.com/watch?v=K35_U80iXwE