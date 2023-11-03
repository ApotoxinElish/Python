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

def caculateMargin(w, dataset, R):
    margin = R
    w_norm = dotProduct(w, w) ** (1 / 2)
    for point in dataset:
        distance = point[-1] * dotProduct(w, point[:-1]) / w_norm
        if distance < margin:
            margin = distance
    return margin


def main(file_name):
    d, n, r, dataset = readData(file_name)

    w, gamma_guess, iter_times = incrementalAlgorithm(d, n, r, dataset)

    margin = caculateMargin(w, dataset, r)
    
    print("----------------------- Result Start -----------------------")
    print(f"The tested file is {file_name}")
    print(f"The Margin Perceptron ends at {iter_times} iterations")
    print(f"The current gamma_guess is {gamma_guess}")
    print(f"The current w is {w}")
    print(f"The current margin is {margin}")
    print("------------------------ Result End ------------------------\n")


if __name__ == "__main__":
    test_files = ["2d-r16-n10000.txt", "4d-r24-n10000.txt", "8d-r12-n10000.txt"]
    print("\nWelcome to use our Margin Perceptron program!\n")
    while True:
        print("Choose one of prepared datasets, or enter another file.\n")
        print("[1] : test on 2d-r16-n10000.txt")
        print("[2] : test on 4d-r24-n10000.txt")
        print("[3] : test on 8d-r12-n10000.txt")
        print("[4] : test on other file")
        print("[5] : exit the program\n")
        try:
            op = int(input("Select the operation you desire: "))
            print()
            if op in range(1, 4):
                main(test_files[op - 1])
            elif op == 4:
                file_name = input("Input the file path of your test file: ")
                main(file_name)
            elif op == 5:
                print("Exit.")
                exit()
            else:
                print("Got undefined input, please retry!")

        except Exception as e:
            print("Got illegal input, please retry!")
