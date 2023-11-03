import numpy as np
from sklearn.svm import SVC
from sklearn.kernel_ridge import KernelRidge


X = np.array(
    [
        [0.4, -0.7],
        [-1.5, -1.0],
        [-1.4, -0.9],
        [-1.3, -1.2],
        [-1.1, -0.2],
        [-1.2, -0.4],
        [-0.5, 1.2],
        [-1.5, 2.1],
        [1.0, 1.0],
        [1.3, 0.8],
        [1.2, 0.5],
        [0.2, -2.0],
        [0.5, -2.4],
        [0.2, -2.3],
        [0.0, -2.7],
        [1.3, 2.1],
    ]
)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])


def build_cauchy_kernel(sigma=1):
    def cauchy_kernel(x1, x2):
        return 1 / (1 + np.linalg.norm(x1 - x2) / sigma**2)

    return cauchy_kernel


def build_cauchy_kernel_SVC(sigma=1):
    def cauchy_kernel_SVC(X, Y):
        result = [[0 for j in range(len(Y))] for i in range(len(X))]
        for i in range(len(X)):
            for j in range(len(Y)):
                result[i][j] = build_cauchy_kernel(sigma)(X[i], Y[j])
        return np.array(result)

    return cauchy_kernel_SVC


def build_locally_periodic_kernel(l=1, p=1):
    def locally_periodic_kernel(x1, x2):
        return np.e ** (
            -2 * np.sin(np.pi * np.linalg.norm(x1 - x2) / p) ** 2 / l**2
        ) * np.e ** (-np.linalg.norm(x1 - x2) / 2 / l**2)

    return locally_periodic_kernel


def build_locally_periodic_kernel_SVC(l=1, p=1):
    def locally_periodic_kernel_SVC(X, Y):
        result = [[0 for j in range(len(Y))] for i in range(len(X))]
        for i in range(len(X)):
            for j in range(len(Y)):
                result[i][j] = build_locally_periodic_kernel(l, p)(X[i], Y[j])
        return np.array(result)

    return locally_periodic_kernel_SVC


if __name__ == "__main__":
    clf = SVC(kernel=build_cauchy_kernel_SVC(sigma=1))
    clf.fit(X, y)
    krr = KernelRidge(kernel=build_cauchy_kernel(sigma=1))
    krr.fit(X, y)

    clf = SVC(kernel=build_locally_periodic_kernel_SVC(l=1, p=1))
    clf.fit(X, y)
    krr = KernelRidge(kernel=build_locally_periodic_kernel(l=1, p=1))
    krr.fit(X, y)
