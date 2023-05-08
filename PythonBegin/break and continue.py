# '''
# 打印楼层的小程序，需求改了。遇到第3层的时候，不打印任何房间号，其他层都打印
# '''
# for i in range(1,10):
#     print(f"---------第{i}层--------")
#     if i == 3:
#         print(f"第{i}层没有房间")
#         continue
#     for j in range(9):
#         print(f"L{i}-{i}0{j} ")



'''
走到404后断掉当前的小循环
'''
for i in range(1,10):
    print(f"---------第{i}层--------")
    if i == 3:
        print(f"第{i}层没有房间")
        continue
    for j in range(9):
        if i == 4 and j == 4:
            print("遇到鬼屋了，over了...")
            break
        print(f"L{i}-{i}0{j} ")