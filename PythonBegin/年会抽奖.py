# '''
# 年会抽奖程序
# 张三科技有限公司有300名员工，开年会抽奖，奖项如下
# 一等奖3名，泰国5日游
# 二等奖6名，iPhone手机
# 三等奖30名，避孕套一盒
#
# 规则：
# 1.共抽3次，第一次抽3等奖，第二次抽2等奖，第3次压轴抽1等奖
# 2.每个员工限中奖一次，不能重复
#
# version:0.1
# author:zhiyu
# '''
#
# import random
# count = 0
# all_staff = list(range(1,301))
# medal1 = "泰国5日游"
# medal2 = "iPhone手机"
# medal3 = "避孕套一盒"
# while count <= 3:
#     count += 1
#     if count == 1:
#         get_person_medal3 = random.sample(all_staff,30)
#         print(f"三等奖中奖的人是{get_person_medal3},奖品是{medal3}")
#         for i in get_person_medal3: #剔除三等奖中奖的人
#             all_staff.remove(i)
#     if count == 2:
#         get_person_medal2 = random.sample(all_staff,6)
#         print(f"二等奖中奖的人是{get_person_medal2},奖品是{medal2}")
#         for i in get_person_medal2: #剔除二等奖中奖的人
#             all_staff.remove(i)
#     if count == 3:
#         get_person_medal1 = random.sample(all_staff,3)
#         print(f"一等奖中奖的人是{get_person_medal1}，奖品是{medal1}")

# '''
# version：0.2
# author：chatGPT
# '''
# import random
#
# all_staff = list(range(1, 301))  # 生成包含所有员工编号的列表
# medal1 = "泰国5日游"
# medal2 = "iPhone手机"
# medal3 = "避孕套一盒"
# winners = []  # 存放所有中奖员工的列表
#
# # 抽奖
# for i in range(3):
#     if i == 0:  # 第一次抽奖
#         get_person_medal3 = random.sample(all_staff, 30)
#         print(f"三等奖中奖的人是{get_person_medal3}，奖品是{medal3}")
#         winners.extend(get_person_medal3)
#     elif i == 1:  # 第二次抽奖
#         remaining_staff = [x for x in all_staff if x not in winners]  # 过滤掉已中奖的员工
#         get_person_medal2 = random.sample(remaining_staff, 6)
#         print(f"二等奖中奖的人是{get_person_medal2}，奖品是{medal2}")
#         winners.extend(get_person_medal2)
#     else:  # 第三次抽奖
#         remaining_staff = [x for x in all_staff if x not in winners]  # 过滤掉已中奖的员工
#         get_person_medal1 = random.sample(remaining_staff, 3)
#         print(f"一等奖中奖的人是{get_person_medal1}，奖品是{medal1}")
#         winners.extend(get_person_medal1)
#
# print("抽奖结束！所有中奖者的编号为：", winners)


'''
version:0.2
author:zhiyu
'''

import random

medal1 = "泰国5日游"
medal2 = "iPhone手机"
medal3 = "避孕套一盒"
winners = []
all_staff = list(range(1,301))
for i in range(3):
    if i == 1:
        get_person_medal3 = random.sample(all_staff,30)
        print(f"三等奖中奖的人是{get_person_medal3},奖品是{medal3}")
        winners.extend(get_person_medal3)
    elif i == 2:
        remaining_staff = [i for i in all_staff if i not in get_person_medal3]
        get_person_medal2 = random.sample(all_staff,6)
        print(f"二等奖中奖的人是{get_person_medal2},奖品是{medal2}")
        winners.extend(get_person_medal2)
    else:
        remaining_staff = [x for x in all_staff if x not in winners]  # 过滤掉已中奖的员工
        get_person_medal1 = random.sample(remaining_staff, 3)
        print(f"一等奖中奖的人是{get_person_medal1}，奖品是{medal1}")
        winners.extend(get_person_medal1)
print(f"所有中奖的人数是：{winners}")







