#!/usr/bin/python3
# -*- encoding:UTF-8 -*-
#Author: BingFengFSX(IFRFSX)<IFRFSX@Protonmail.com>
#License: Beer-ware Software License

 #
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # <phk@FreeBSD.ORG> wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return.   Poul-Henning Kamp
 # ----------------------------------------------------------------------------
 #

import os

if os.access("./SSL文件",os.F_OK):
    pass
else:
    os.mkdir("./SSL文件")

print("""欢迎使用SSL证书生成器！
在使用前，请确保您的计算机安装了openssl.
使用的时候，请按住回车键。""")
num = eval(input("请问您打算生成多少ssl证书："))
bite = eval(input("请问您打算生成多少位宽的ssl证书："))
for fx in range(num):
    os.system("openssl req -newkey rsa:%d -nodes -x509 -keyout ./SSL文件/编号[%d]SSL密钥.key -out ./SSL文件/编号[%d]SSL证书.crt -days 999999" % (bite,fx,fx))
    print("已生成编号："+str(fx))
else:
    print("生成完毕。")
