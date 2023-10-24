# Margin Perceptron

Our program supports the test sets provided by the operation questions and all test sets that meet the following requirements:

- The first line contains three numbers n, d, and r, where n is the number of points, d is the dimensionality of the instance space, and r is the radius.
- The i-th line (where i goes from 2 to n + 1) gives the (i - 1)-th point in the dataset as: $x_1,x_2,...,x_d,label$ where the first d values are the coordinates of the point, and label = 1 or -1.
- The test sets should be linearly separable.
  
Our program is simple to use, just run the Python program directly, and then enter the command number/test file path as prompted.  Here are usage examples:

```
Welcome to use our Margin Perceptron program!
1: test on 2d-r16-n10000.txt
2: test on 4d-r24-n10000.txt
3: test on 8d-r12-n10000.txt
4: test on other file
5: exit the program
Select the operation you desire:1
----------------------- Result Start -----------------------
The tested file is 2d-r16-n10000.txt
The Margin Perceptron ends at 8 iterations
The current gamma_guess is 4.0
The current w is [4.0068648583112605, -40.90265408362018]
------------------------ Result End ------------------------
1: test on 2d-r16-n10000.txt
2: test on 4d-r24-n10000.txt
3: test on 8d-r12-n10000.txt
4: test on other file
5: exit the program
Select the operation you desire:2
----------------------- Result Start -----------------------
The tested file is 4d-r24-n10000.txt
The Margin Perceptron ends at 17 iterations
The current gamma_guess is 12.0
The current w is [25.373182021799593, -69.8062667042172, -99.63600352277491, 83.14303873000287]
------------------------ Result End ------------------------
1: test on 2d-r16-n10000.txt
2: test on 4d-r24-n10000.txt
3: test on 8d-r12-n10000.txt
4: test on other file
5: exit the program
Select the operation you desire:3
----------------------- Result Start -----------------------
The tested file is 8d-r12-n10000.txt
The Margin Perceptron ends at 25 iterations
The current gamma_guess is 6.0
The current w is [-14.441350112907852, -21.51688504945141, -45.299145496891654, -11.840703142819663, 59.964400115003855, 34.7456353719872, 55.02649341178936, -15.023153799930784]
------------------------ Result End ------------------------
1: test on 2d-r16-n10000.txt
2: test on 4d-r24-n10000.txt
3: test on 8d-r12-n10000.txt
4: test on other file
5: exit the program
Select the operation you desire:4
Input the file path of your test file:2d-r16-n10000.txt
----------------------- Result Start -----------------------
The tested file is 2d-r16-n10000.txt
The Margin Perceptron ends at 8 iterations
The current gamma_guess is 4.0
The current w is [4.0068648583112605, -40.90265408362018]
------------------------ Result End ------------------------
1: test on 2d-r16-n10000.txt
2: test on 4d-r24-n10000.txt
3: test on 8d-r12-n10000.txt
4: test on other file
5: exit the program
Select the operation you desire:5
Exit
```