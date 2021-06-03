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
num = int(input("请问您打算生成多少ssl证书："))
bite = str(input("请问您打算生成哪种类型的ssl证书\n（例如：prime256v1、secp521r1）："))
for fx in range(num):
    os.system("openssl ecparam -genkey -name %s -out ./SSL文件/%d.key" % (bite,fx))
    os.system("openssl req -new -key ./SSL文件/%d.key -out ./SSL文件/%d.crt -x509 -nodes -days 999999" % (fx,fx))
    print("已生成编号："+str(fx))
else:
    print("生成完毕。")
