# -*- coding: UTF-8 -*-

# author by : （学员ID)
# 目的
# 写一张小学四则运算题


# 导入random（随机数）模块
import random

# print("-----小学四则运算题-----")
filename1= "小学数学卷.txt"
f1= open(filename1, 'w')  # write 方式第一次写一行
line1 = "-----小学四则运算题-----\n"
f1.write(line1)
f1.close()

# 向文件追加内容
filename2= "小学数学卷（2）.txt"
f2= open(filename2, 'w')  # write 方式第一次写一行
line2 = "-----小学四则运算题（答案）-----\n"
f2.write(line2)
f2.close()



#---------------------
f1= open(filename1, 'a') # append 方式读文件
f2= open(filename2, 'a') # append 方式读文件

total=0

for row in range(1,21):
    line1 = ""
    line2 = ''
    for col in range(1,6):
        total=total+1

        #随机生成2个0-99之间的整数
        a = random.randint(1, 99)
        b = random.randint(1, 99)

        #随机生成运算符
        op = random.randint(1, 4)

        if op == 1:
            line1 = line1 + "%02d + %02d= \t" % (a,b)
            # print(line1)
            c = a + b
            line2 = line2 + "%02d + %02d = %02d \t" % (a,b,c )

        if op == 2:
            line1 = line1 + "%02d - %02d = \t" % (a,b)
            # print(line1)
            c = a - b
            line2 = line2 + "%02d - %02d = %02d \t" % (a,b,c )

        if op == 3:
            line1 = line1 + "%02d × %02d = \t" % (a,b)
            # print(line1
            c = a * b
            line2 = line2 + "%02d × %02d = %02d \t" % (a,b,c )

        if op == 4:
            line1 = line1 + "%02d ÷ %002d = \t" % (a,b)
            c = a / b
            line2 = line2 + "%02d ÷ %02d = %02d \t" % (a,b,c )


    # print(line1)
    line1 = line1 + '\n'
    f1.write(line1)
    line2 = line2 + '\n'
    f2.write(line2)
# print("\n")
        #print("现在打印第{0}行-第{1}列-第{2}题\t\t\t".format(row,col,total))



# print("-----结束---总共出了{0}道四则运算题".format(total))
filename1 = "-----结束---总共出了{0}道四则运算题---\n".format(total)
f1.write(filename1)
filename2 = "-----结束---总共出了{0}道四则运算题含答案---\n".format(total)
f2.write(filename2)

f1.close()
f2.close()
