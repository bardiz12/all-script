#!/usr/bin/env python3
import os,sys


if len(sys.argv) < 1 :
    print("usage: python3 sendENV.py .env_file")
    exit()


env = open(sys.argv[1],'r').read()
envs = env.splitlines()

for env in envs:
    parsed = env.split("=",1)
    if(len(parsed) > 1):
        key = parsed[0]
        value = parsed[1]
        if(value != ""):
            print(env)
            os.system("heroku config:set " + env)