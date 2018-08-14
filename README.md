# Machine Learning in Python
Implementing Machine Learning algorithms and techniques in Python.

### Reference to:
Valentyn N Sichkar. Machine Learning in Python // GitHub platform

## Description
Practical experiments on Machine Learning in Python.

## Content
Codes (it'll send you to appropriate file):
* [Processing_Sentences](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Codes/Processing_Sentences.py)
* [Function_approximation](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Codes/Function_approximation.py)

<br/>
Experimental results (figures and tables on this page):

* <a href="#Processing sentences and finding cosine distances">Processing sentences and finding cosine distances</a>
* <a href="#Approximation of functions via linear equations">Approximation of functions via linear equations</a>

### <a name="Processing sentences and finding cosine distances">Processing sentences and finding cosine distances</a>
Implementing the task about processing sentences. Finding cosine distances between first sentence and all others. For implementation a two-dimensional matrix is created, where rows are sentences (objects) and columns are words (properties).
<br/>Matrix is filled with numbers that corresponds to number of times every word (property) were met in every sentence. Then, after matrix was built, distances are calculated between first vector (row) and all others. Calculation is done with the help of **'scipy.spatial.distance.cosine'** function.
<br/><br/>Part of the code is shown below with a lot of comments:

```py
from scipy.spatial.distance import cosine

# Calculating cosine distances between first sentence and all others
# Writing result into new dictionary
# Indexes of sentences are keys and distances are values
# Also, writing result into list, that will help to find two minimums
d = {}
lst_distances = []
for i in range(1, len(a)):
    c = cosine(a[0, :], a[i, :])
    d[i] = c
    lst_distances += [c]

# Finding two sentences with closest distances to the first one
# Sorting the list with the method 'sort()'
lst_distances.sort()  # All elements are sorted now by increasing

# Finding keys from the dictionary that are corresponds to two first elements from the list
result_1 = list(d.keys())[list(d.values()).index(lst_distances[0])]
result_2 = list(d.keys())[list(d.values()).index(lst_distances[1])]

print(result_1, result_2)  # Number of closest sentences
print(d)

```

As a result, dictionary is obtained with number of sentence as a key (from number 1) and distance to the very first sentence (number 0):
<br/>{1: 0.9527544408738466, 2: 0.8644738145642124, 3: 0.8951715163278082, 4: 0.7770887149698589, 5: 0.9402385695332803, 6: 0.7327387580875756, 7: 0.9258750683338899, 8: 0.8842724875284311, 9: 0.9055088817476932, 10: 0.8328165362273942, 11: 0.8804771390665607, 12: 0.8396432548525454, 13: 0.8703592552895671, 14: 0.8740118423302576, 15: 0.9442721787424647, 16: 0.8406361854220809, 17: 0.956644501523794, 18: 0.9442721787424647, 19: 0.8885443574849294, 20: 0.8427572744917122, 21: 0.8250364469440588}

Then, two closest sentences to the 0-numbered sentence were found as a result.

Full code is available here: [Processing_Sentences.py](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Codes/Processing_Sentences.py)

### <a name="Approximation of functions via linear equations">Approximation of functions via linear equations</a>
Implementing the task for approximation of function with linear equations. Using first degree polynomial, second degree polynomial and third degree polynomial. Solving equations with matrix method via **'numpy.linalg.solve(a, b)'** function.

Initial function is as following:
<br/>**f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)**

Points for first degree polynomials are: **1, 15**
<br/>Points for second degree polynomials are: **1, 8, 15**
<br/>Points for third degree polynomials are: **1, 4, 10, 15**
<br/><br/>Part of the code is shown below with a lot of comments:

```py
import numpy as np


# Creating first degree polynomials in the points of 1 and 15
# It has to be in following form:
# w_0 + w_1 * x_1 = y_1
# w_0 + w_1 * x_2 = y_2
# Writing systems of equations into two-dimensional array 'a' and vector 'b'
a = np.array([[1, 1], [1, 15]])
b = np.array([f(1), f(15)])  # [3.25221687 0.63522142]

# Solving system of linear equations for first degree polynomial
w = np.linalg.solve(a, b)  # [ 3.43914511 -0.18692825]
# Found equation for the first degree polynomial is as following:
# y = w[0] + w[1] * x

```

Results are plot in order to understand the quality of approximation in eche case. Figure is shown below

![Approximation_of_function](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/images/Approximation_of_function.png)

Full code is available here: [Function_approximation.py](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Codes/Function_approximation.py)

<br/>

### MIT License
### Copyright (c) 2018 Valentyn N Sichkar
### github.com/sichkar-valentyn
### Reference to:
Valentyn N Sichkar. Machine Learning in Python // GitHub platform
