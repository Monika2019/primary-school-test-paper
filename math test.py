# -*- coding: UTF-8 -*-

# author by : （学员ID)
# 目的
# 写一张小学四则运算题


# 导入random（随机数）模块
import random

# print("-----小学四则运算题-----")
filename = "小学数学卷.txt"
f = open(filename, 'w')  # write 方式第一次写一行

text2write = "-----小学四则运算题-----\n"

f.write(text2write)

f.close()
# 向文件追加内容
f = open(filename, 'a') # append 方式读文件


total=0

# for i in range(1,100)

for row in range(1,21):
    line1 = ""
    for col in range(1,6):
        total=total+1

        #随机生成2个0-99之间的整数
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        #随机生成运算符
        op = random.randint(1, 4)

        if op == 1:
            line1 = line1 + "%d + %d = \t" % (a,b)
            # print(line1)

        if op == 2:
            line1 = line1 + "%d - %d = \t" % (a,b)
            # print(line1)

        if op == 3:
            line1 = line1 + "%d * %d = \t" % (a,b)
            # print(line1)

        if op == 4:
            line1 = line1 + "%d / %d = \t" % (a,b)
    # print(line1)
    text2write = line1 + '\n'
    f.write(text2write)
# print("\n")
        #print("现在打印第{0}行-第{1}列-第{2}题\t\t\t".format(row,col,total))



# print("-----结束---总共出了{0}道四则运算题".format(total))
text2write = "-----结束---总共出了{0}道四则运算题---\n".format(total)
f.write(text2write)

f.close()
