# '''
# 猜年龄
# '''
# black_girl_age = 25
# for i in range(10):
#     guess = int(input("请输入你猜的年龄："))
#     if guess < black_girl_age:
#         print("哎呀，我没有这么年轻")
#     elif guess > black_girl_age:
#         print("我有这么老嘛")
#     else:
#         exit("恭喜你，终于猜对了")


# '''
# 从0-100的奇偶数
# '''
# for i in range(101):
#     if i % 2 == 0:
#         print(f"{i}是偶数")

# '''
# 打印各楼层房
# '''
# for i in range(1,10):
#     for j in range(6):
#         print(f"L{i}-{i}0{j}",end= " ")
#     print()

'''
打印3角形
'''
for i in range(1,10):
    if i <= 5:
        print("*"*i)
    else:
        print("*"*(10-i))