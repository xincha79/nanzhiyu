# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 18:08
# @Author  : 南知渔
# @File    : 2进制模式操作文件.py
# @Software: PyCharm

'''
用Python操作图片
'''
# rb 二进制写
# f = open("桌面图片.png","rb")
# for line in f:
#     print(line)

# wb 二进制写
# f = open("wb.file","wb")
# s = "路飞"
# f.write(s.encode("utf-8"))


'''
跳到任意位置修改
'''
# f = open("name_list",encoding="utf-8")
# f.seek(12)
# print(f.readline())

# 写
# f = open("seek_write","w")
# f.write("hello1\n")
# f.write("hello2\n")
# print("返回当前光标位置：",f.tell())
# f.write("hello3\n")
# print("返回当前光标位置：",f.tell())
# f.seek(14)
# f.write("------")

#flush