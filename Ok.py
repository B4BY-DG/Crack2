#coding=utf-8
 
import os,sys,random,struct
 
x = str(struct.calcsize("P") * 8)

if '64' in x:
 
    os.system('chmod 777 s64 && ./s64')
 
else:
 
    print('\033[1;31m   please change ur phone then try again\033[0;97m')
    os.system('xdg-open https://facebook.com/groups/1267278830395332/')
    os.sys.exit()
 
 
