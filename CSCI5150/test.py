import numpy as np
from sklearn import svm, datasets
from matplotlib.pylab import plt


if __name__ == "__main__":
    X_train = np.array([[0.3, 0.4], [0, 0], [1, 1], [1.1, 1.1]])
    y_train = [0, 0, 1, 1]
    X_test = np.array([[0.2, 0.2], [0, 3], [1, -1], [5, 5]])
    y_test = [0, 1, 0, 1]

    def my_kernel(X, Y):
        print(X)
        print(Y)
        print(np.dot(X, Y.T))
        return np.dot(X, Y.T)

    clf = svm.SVC(kernel=my_kernel)
    clf.fit(X_train, y_train)
    result = clf.predict(X_test)
    print(result)
