
import random
print("**********欢迎来到剪刀石头布**********")
a, b, c, d="剪刀", "石头", "布", "不玩了"
m = 0
computer = 0
user = 0
while m != d:
    z = random.choice([a, b, c])
    # print("系统出的%s" % z)
    n = input("请输入你的手势：")
    if n == a and z == c or n == b and z == a or n == c and z == b:
        print("你出的%s，系统出的%s 你赢了" % (n, z))
        user += 1
    elif n == a and z == b or n == b and z == c or n == c and z == a:
        print("你出的%s，系统出的%s 你输了" % (n, z))
        computer += 1
    else:
        print("你出的%s，系统出的%s 平局" % (n, z))
    print("您与系统的比分为：%d：%d" % (user, computer))
    m = input("还玩吗？")
    if m == d:
        break
print("您与系统最终比分为%d：%d" % (user, computer))
print("************大爷有空再来啊************")

