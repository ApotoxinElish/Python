# Q2

# Using Custom Kernel Functions with scikit-learn

This code demonstrates how to use the implemented custom kernel functions with the scikit-learn APIs, specifically `sklearn.svm.SVC` (kernel SVMs) and `sklearn.kernel_ridge.KernelRidge` (kernel regularized linear regression).

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- NumPy
- scikit-learn

## Usage

1. Import the necessary modules:

```python
import numpy as np
from sklearn.svm import SVC
from sklearn.kernel_ridge import KernelRidge
```

2. Define your dataset. The example code provides a sample dataset X and corresponding labels y.

3. The code provides two kernel functions:

   - For "sklearn.svm.SVC"

     - build_cauchy_kernel_SVC(sigma=1)

     - build_locally_periodic_kernel_SVC(l=1, p=1)

   - For "sklearn.kernel_ridge.KernelRidge"

     - build_cauchy_kernel(sigma=1)

     - build_locally_periodic_kernel(l=1, p=1)

   These functions create and return the custom kernel functions based on the specified parameters.

4. Instantiate and train the models using the custom kernel functions.

   - SVC using the Cauchy kernel:

   ```python
   clf = SVC(kernel=build_cauchy_kernel_SVC(sigma=1))
   clf.fit(X, y)
   ```

   - Kernel Ridge using the Cauchy kernel:

   ```python
   krr = KernelRidge(kernel=build_cauchy_kernel(sigma=1))
   krr.fit(X, y)
   ```

   - SVC using the Locally Periodic kernel:

   ```python
   clf = SVC(kernel=build_locally_periodic_kernel_SVC(l=1, p=1))
   clf.fit(X, y)
   ```

   - Kernel Ridge using the Locally Periodic kernel:

   ```python
   krr = KernelRidge(kernel=build_locally_periodic_kernel(l=1, p=1))
   krr.fit(X, y)
   ```

   You can simply change the coefficients _sigma_, _l_, _p_ for different uses.
