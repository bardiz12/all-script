import os,sys,requests
import urllib.parse
import html

if (len(sys.argv) < 2):
    print("Usage : python cmd.py [URL]")
    exit()
url = sys.argv[1]

while True:
    a = input("> ")
    print(requests.get(url+urllib.parse.quote(a)).text)