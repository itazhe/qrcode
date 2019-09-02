#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能：二维码生成器
作者：azhe
时间：2019-7-23 14:47
邮箱:

'''


import qrcode


data = input("请输入要生成二维码的内容：")

img = qrcode.make(data)

img.save("qr.jpg")

print("成功生成二维码图片(qr.jpg)!")

input("\n按回车键退出.......")

