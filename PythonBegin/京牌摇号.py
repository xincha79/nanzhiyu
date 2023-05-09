# '''
# 京牌摇号
# version 0.1
# author:zhiyu
# '''
import  string
import random
#
# count = 0
# while count < 3:
#     count +=1
#     card = 0
#     while card <= 20:
#         card += 1
#         x1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#         s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#         x2 = random.sample(s,5)
#         x3 ="".join(x2)
#         print(f"京{x1} {x3}")
#     user = str(input("输入你看上的车牌号"))

'''
京牌摇号
version 0.2
author：zhiyu
'''

count = 0
while count <= 3:
    car_nums = []
    count += 1
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_uppercase+string.digits,5))
        c_num = f"京{n1}-{n2}"
        car_nums.append(c_num)
        print(c_num)
    choice = str(input("请输入你喜欢的车牌"))
    if choice in car_nums:
        print("恭喜你选择成功")
        exit("Good,luck!")
    else:
        print("请继续选择")