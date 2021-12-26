def main():
    # n个学生, m条信息
    n, m = [int(i) for i in input().split(" ")]
    messages = []
    for i in range(m):
        messages.append([int(j) for j in input().split(" ")])

    # print(messages)

    real_message = {}
    for i in range(1, m):
        if messages[i][2] == messages[i - 1][2]:
            l = max(messages[i][0], messages[i - 1][0])
            r = min(messages[

        else:
        



main()
