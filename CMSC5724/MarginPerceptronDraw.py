import matplotlib.pyplot as plt
import numpy as np


def readData(file_name):
    with open(file_name) as f:
        first_line = f.readline()
        dataset = f.read().split("\n")

    d, n, r = [int(each) for each in first_line.split(",")]

    for i, line in enumerate(dataset):
        dataset[i] = [eval(each) for each in line.split(",")]
    # print(dataset)

    return d, n, r, dataset


def dotProduct(vector1, vector2):
    dot_product = 0
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
    return dot_product


def findViolationPoint(gamma_guess, w, dataset):
    w_norm = dotProduct(w, w) ** (1 / 2)
    if not w_norm:
        return dataset[0]

    for point in dataset:
        distance = point[-1] * dotProduct(w, point[:-1]) / w_norm

        if distance < gamma_guess / 2:
            return point

    return None


def adjustW(w, p):
    for i, each in enumerate(w):
        w[i] = each + p[-1] * p[i]

    return w


def marginPerceptron(gamma_guess, d, n, R, dataset):
    w = [0 for i in range(d)]
    iter_limit = 12 * R**2 / gamma_guess**2

    iter_times = 0
    while iter_times <= iter_limit:
        p = findViolationPoint(gamma_guess, w, dataset)
        # print(p)
        if not p:
            break

        w = adjustW(w, p)
        # print(w)
        iter_times += 1

    if iter_times > iter_limit:
        return None, iter_times
    else:
        return w, iter_times


def incrementalAlgorithm(d, n, R, dataset):
    gamma_guess = R
    w = None

    while True:
        w, iter_times = marginPerceptron(gamma_guess, d, n, R, dataset)
        # print(w)
        if w:
            break

        gamma_guess /= 2

    return w, gamma_guess, iter_times


def drawPlane(w, dataset):
    fig, ax = plt.subplots()

    x = [each[0] for each in dataset]
    y = [each[1] for each in dataset]
    label = ["green" if each[-1] + 1 else "blue" for each in dataset]
    ax.scatter(x, y, s=2, c=label)

    x = np.linspace(-16, 16, 100)
    y = -w[0] * x / w[1]
    ax.plot(x, y, linewidth=2.0, color="red")

    plt.show()


def main():
    file_name = "2d-r16-n10000.txt"
    # file_name = "4d-r24-n10000.txt"
    # file_name = "8d-r12-n10000.txt"

    d, n, r, dataset = readData(file_name)

    w, gamma_guess, iter_times = incrementalAlgorithm(d, n, r, dataset)
    print(
        "The Margin Perceptron ends at "
        + str(iter_times)
        + " iterations: The current gamma_guess is "
        + str(gamma_guess)
        + " and current w is "
        + str(w)
        + "."
    )

    drawPlane(w, dataset)


if __name__ == "__main__":
    main()
