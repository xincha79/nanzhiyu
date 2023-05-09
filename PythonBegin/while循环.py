# '''
# 死循环
# '''
# count = 0
# while count <= 18:
#     count += 1
#     print(f"这是第{count}次循环")

# '''
# 猜年龄
# '''
# black_girl_age = 25
# count = 0
# while count <= 5:
#     count += 1
#     guess = int(input('请输入你的猜测'))
#     if guess < black_girl_age:
#         print("哎呀，我没有这么年轻")
#     elif guess > black_girl_age:
#         print("我有这么老嘛")
#     else:
#         print("恭喜你，终于猜对了")
#         break
# if count > 3:
#     print("你真是太笨啦")

'''
九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i * j} ",end="")
    print()

