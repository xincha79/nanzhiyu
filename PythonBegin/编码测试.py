# -*- encoding:utf-8 -*-

# s = "南知渔"
# print(s)  #unicode

# gbk_2_unicode = s.decode("gbk")
# print(gbk_2_unicode)  #python3执行不了

# f = open("name_list",mode="w")
#
# f.write("南知渔\n")
# f.write("山谷\n")
#
# f.close()

# f = open("name_list",mode="r")
# print(f.readline()) #读一行
# print('--------------')
# print(f.read()) #读出所有内容
# f.write("ee")

# f = open("name_list","a")
# f.write("lumos\n")
# f.write("Valleya\n")
# f.close()
# f.read()

f = open("模特数据",encoding="utf-8")

for line in f:
    line=line.split()
    print(line)
