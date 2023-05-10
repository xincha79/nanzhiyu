# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 17:14
# @Author  : 南知渔
# @File    : 全局文本检索替换.py
# @Software: PyCharm

'''
全局文本检索替换
写一个脚本，允许用户按意向方式执行，即对制定文件内容进行全局替换，且替换完毕后打印替换多少处内容
写完后脚本调用方式
python your_script.py old_str new_str filename
'''
import sys
print(sys.argv)


# old_str = sys.argv[1]
# new_str = sys.argv[2]
# filename = sys.argv[3]
#
# #读取内存
# f = open(filename,"r+")
# data = f.read()
#
#
# #统计替换字符
# old_str_count = data.count(old_str)
# new_data = data.replace(old_str,new_str)
#
# #删除旧文件
# f.seek(0)
# f.truncate()
#
# #写入新文件
# f.write(new_data)
#
# print(f"原表达式为{old_str},替换为{new_str},次数是{old_str_count}")





