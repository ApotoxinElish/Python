day = 1
while day <= 7:
    answer = input("今天有好好学习吗？")
    if answer != "有":
        break
    day += 1
else:
    print("非常棒，你已经坚持了7天连续学习！")
