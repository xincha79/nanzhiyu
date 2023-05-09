'''
现要求按考试成绩按成员高低将学员们分成5组，全存在一个新的大列表里，5组分别是90-100，80-89,70-79,60-69,0-59
最终的数据格式如下：
new_stu_list = [
    [
        ["Alex",100],
        ["Rain",91],
    ],
    [
        ["银角",79],
        ["Jack",78],
    ],
    ....
    ....
]
version:1.0
author:zhiyu
'''
stu_list=[['张三', 72], ['李四', 89], ['王五', 54], ['赵六', 76], ['钱七', 68], ['孙八', 93], ['周九', 81], ['吴十', 67], ['郑十一', 73], ['冯十二', 56],
['陈十三', 85], ['楚十四', 91], ['卫十五', 78], ['蒋十六', 62], ['沈十七', 77], ['韩十八', 58], ['杨十九', 84], ['朱二十', 80], ['秦二十一', 69], ['尤二十二', 74],
['许二十三', 71], ['何二十四', 87], ['吕二十五', 63], ['施二十六', 79], ['张二十七', 65], ['孔二十八', 70], ['曹二十九', 55], ['严三十', 90], ['华三十一', 75], ['金三十二', 92],
['魏三十三', 61], ['陶三十四', 86], ['姜三十五', 82], ['戚三十六', 57], ['谢三十七', 83], ['邹三十八', 64], ['喻三十九', 88], ['柏四十', 59], ['水四十一', 70], ['窦四十二', 75],
['章四十三', 87], ['云四十四', 66], ['苏四十五', 73], ['潘四十六', 80], ['葛四十七', 81], ['奚四十八', 92], ['范四十九', 79], ['彭五十', 89]]

# group1 = []
# group2 = []
# group3 = []
# group4 = []
# group5 = []
# new_stu_list = []
#
# for x in stu_list:
#     if x[1] > 90:
#         group1.append(x)
#     elif x[1] > 80:
#         group2.append(x)
#     elif x[1] > 70:
#         group3.append(x)
#     elif x[1] > 60:
#         group4.append(x)
#     else:
#         group5.append(x)
# print(group1)
# new_stu_list.extend(group1)
# new_stu_list.extend(group2)
# new_stu_list.extend(group3)
# new_stu_list.extend(group4)
# new_stu_list.extend(group5)
#
# for i in new_stu_list:
#     print(i)

'''
version:2.0
author:zhiyu
'''
stu_groups =[
    [], #90分以上
    [], #80分以上
    [], #70分以上
    [], #60分以上
    []
]

for i in stu_list:
    if i[1] >= 90:
        stu_groups[0].append(i)
    elif i[1] >= 80:
        stu_groups[1].append(i)
    elif i[1] >= 70:
        stu_groups[2].append(i)
    elif i[1] >= 60:
        stu_groups[3].append(i)
    else:
        stu_groups[4].append(i)


for i in stu_groups:
    print(i)