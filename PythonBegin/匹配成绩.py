'''
成绩有ABCD 5个等级，与分数的对应关系如下
A 90-100
B 80-89
C 60-79
D 40-59
E 0-39
'''

score = int(input("请输入你的成绩"))
if score > 90:
    print("A")
elif score >80:
    print("B")
elif score > 60:
    print("C")
elif score > 40:
    print("D")
else:
    print("E")
