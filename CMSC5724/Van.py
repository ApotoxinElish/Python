import matplotlib.pyplot as plt
import numpy as np


def drawPlane(y1, y2):
    fig, ax = plt.subplots()
    x = [i for i in range(len(y1))]
    ax.plot(x, y1)
    ax.plot(x, y2)
    plt.show()


def main():
    Y1 = []
    Y2 = []
    for i in range(100):
        if i <= 10:
            y1 = 59
        elif i <= 20:
            y1 = 59 + (i - 10) * 4.2
        elif i <= 50:
            y1 = i * 4.2
        elif i <= 70:
            y1 = i * 3.9
        elif i <= 100:
            y1 = i * 3.6
        elif i <= 300:
            y1 = i * 3.3
        elif i <= 500:
            y1 = i * 2.4
        elif i <= 1000:
            y1 = i * 1.8
        else:
            y1 = i * 1.5

        # for i in range(100):
        if i <= 1:
            y2 = 9
        elif i <= 20:
            y2 = 9 + (i - 1) * 4.5
        else:
            y2 = 9 + (i - 1) * 4.5

        Y1.append(y1)
        Y2.append(y2)
    # print(data)
    drawPlane(Y1, Y2)


if __name__ == "__main__":
    main()
