# File: Function_approximation.py
# Description: Approximation of function with the help of system of linear equations
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# Valentyn N Sichkar. Machine Learning in Python // GitHub platform. DOI: 10.5281/zenodo.1345027




# Implementing the task
# Approximation function with linear equations
# Solving equations with matrix method
# Using function 'numpy.linalg.solve(a, b)'


import math
import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


# Initial function
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
def f(k):
    return math.sin(k / 5) * math.exp(k / 10) + 5 * math.exp(-k / 2)


# Function to return array with 'y' results from input array of 'x' for plotting
def f_array(k):
    return np.sin(k / 5) * np.exp(k / 10) + 5 * np.exp(-k / 2)


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


# Creating second degree polynomials in the points of 1, 8 and 15
# It has to be in following form:
# w_0 + w_1 * x_1 + w_2 * x_1 * x_1 = y_1
# w_0 + w_1 * x_2 + w_2 * x_2 * x_2 = y_2
# w_0 + w_1 * x_3 + w_2 * x_3 * x_3 = y_3
# Writing systems of equations into three-dimensional array 'a' and vector 'b'
a = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 225]])
b = np.array([f(1), f(8), f(15)])  # [3.25221687 2.31617016 0.63522142]

# Solving system of linear equations for second degree polynomial
ww = np.linalg.solve(a, b)  # [ 3.32512949 -0.06531159 -0.00760104]
# Found equation for the second degree polynomial is as following:
# y = ww[0] + ww[1] * x + ww[2] * x * x


# Creating third degree polynomials in the points of 1, 4, 10 and 15
# It has to be in following form:
# w_0 + w_1 * x_1 + w_2 * x_1 * x_1 + w_3 * x_1 * x_1 * x_1 = y_1
# w_0 + w_1 * x_2 + w_2 * x_2 * x_2 + w_3 * x_2 * x_2 * x_2 = y_2
# w_0 + w_1 * x_3 + w_2 * x_3 * x_3 + w_3 * x_3 * x_3 * x_3 = y_3
# w_0 + w_1 * x_4 + w_2 * x_4 * x_4 + w_3 * x_4 * x_4 * x_4 = y_4
# Writing systems of equations into four-dimensional array 'a' and vector 'b'
a = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = np.array([f(1), f(4), f(10), f(15)])  # [3.25221687 1.74684595 2.50541641 0.63522142]

# Solving system of linear equations for third degree polynomial
www = scipy.linalg.solve(a, b)  # [ 4.36264154 -1.29552587  0.19333685 -0.00823565]
# Found equation for the second degree polynomial is as following:
# y = www[0] + www[1] * x + www[2] * x * x + www[3] * x * x * x

# Plotting found functions and compare them with original one
# Creating a figure with subplots
figure, ax = plt.subplots(nrows=2, ncols=2)
# ax is (2, 2) np array and to make it easier to read we use 'flatten' function
# Or we can call each time ax[0, 0]
ax0, ax1, ax2, ax3 = ax.flatten()

# Preparing arrays for plotting original function
x = np.arange(1, 15.1, 0.1)
y = f_array(x)

# Preparing array for plotting obtained first degree polynomial
y_1 = w[0] + w[1] * x

# Preparing array for plotting obtained second degree polynomial
y_2 = ww[0] + ww[1] * x + ww[2] * x * x

# Preparing array for plotting obtained third degree polynomial
y_3 = www[0] + www[1] * x + www[2] * x * x + www[3] * x * x * x

# Adjusting first subplot
ax0.plot(x, y, 'b')
ax0.set_xlabel('')
ax0.set_ylabel('')
ax0.set_title('Original function')

# Adjusting second subplot
ax1.plot(x, y_1, 'r', x, y, 'b')
ax1.set_xlabel('')
ax1.set_ylabel('')
ax1.set_title('First degree polynomial')

# Adjusting third subplot
ax2.plot(x, y_2, 'r', x, y, 'b')
ax2.set_xlabel('')
ax2.set_ylabel('')
ax2.set_title('Second degree polynomial')

# Adjusting fourth subplot
ax3.plot(x, y_3, 'r', x, y, 'b')
ax3.set_xlabel('')
ax3.set_ylabel('')
ax3.set_title('Third degree polynomial')

# Function to make distance between figures
plt.tight_layout()
# Giving the name to the window with figure
figure.canvas.set_window_title('Approximation of function with linear equations')
# Showing the plots
plt.show()
