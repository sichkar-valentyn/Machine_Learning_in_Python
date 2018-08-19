# File: Function_Optimization.py
# Description: Optimization of smooth and non-smooth functions with 'BFGS' and 'differential evolution' methods
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# Valentyn N Sichkar. Machine Learning in Python // GitHub platform. DOI: 10.5281/zenodo.1345027




# Implementing the task
# Optimization of smooth and non-smooth functions


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


# Task 1 - smooth function
# Initial smooth function
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
# Function returns array with 'y' results from input array of 'x' for plotting by using 'np' instead of 'math'
def f_array(k):
    return np.sin(k / 5) * np.exp(k / 10) + 5 * np.exp(-k / 2)


# Finding minimum of smooth function with 'BFGS' method
# Setting initial point in form of 'ndarray' as 'minimize' function requires it in form of 'ndarray'
x0_start = np.array([2])
# print(type(x))  -->  <class 'numpy.ndarray'>
# print(x.shape)  -->  (1,)
# Finding minimum of the function from starting point 'x_start = 2'
# Using 'minimize' function from 'scipy.optimize' library
y0_min = optimize.minimize(f_array, x0_start, method='BFGS')
print(y0_min)  # fun = 1.7452682903449388, iterations = 6
print()


# Setting initial point in form of 'ndarray' as 'minimize' function requires it in form of 'ndarray'
x1_start = np.array([30])
# print(type(x))  -->  <class 'numpy.ndarray'>
# print(x.shape)  -->  (1,)
# Finding minimum of smooth function from starting point 'x_start = 30'
# Using 'minimize' function from 'scipy.optimize' library
y1_min = optimize.minimize(f_array, x1_start, method='BFGS')
print(y1_min)  # fun = -11.898894665981285, iterations = 6
print()


# Finding minimum of smooth function with 'differential evolution' method
# Searching in the range [1, 30]
# Setting the range for searching in form of tuple inside list as function requires it
x2_range = [(1, 30)]  # tuple inside list
# Finding minimum of smooth function
y2_min = optimize.differential_evolution(f_array, [(1, 30)])
print(y2_min)  # fun = -11.89889467, iterations = 5
print()


# Task 2 - non-smooth function
# Initial non-smooth function
# We take here the same function but only with integer results
# By using 'np.int_' we return 'numpy.ndarray' of integer numbers
def h_array(k):
    return np.int_(f_array(k))


# Finding minimum of non-smooth function with 'BFGS' method
# Setting initial point in form of 'ndarray' as 'minimize' function requires it in form of 'ndarray'
x3_start = np.array([30])
# print(type(x))  -->  <class 'numpy.ndarray'>
# print(x.shape)  -->  (1,)
# Finding minimum of the function from starting point 'x_start = 30'
# Using 'minimize' function from 'scipy.optimize' library
y3_min = optimize.minimize(h_array, x3_start, method='BFGS')
print(y3_min)  # fun = -5, iterations = 0
print()

# Finding minimum of non-smooth function with 'differential evolution' method
# Searching in the range [1, 30]
# Setting the range for searching in form of tuple inside list as function requires it
x4_range = [(1, 30)]  # tuple inside list
# Finding minimum of smooth function
y4_min = optimize.differential_evolution(h_array, [(1, 30)])
print(y4_min)  # fun = -11.0, iterations = 3
print()

# Plotting smooth and non-smooth functions with found points
# Creating a figure with subplots
figure, ax = plt.subplots(nrows=1, ncols=2)
# ax is (1, 2) np array and to make it easier to read we use 'flatten' function
# Or we can call each time ax[0, 0]
ax0, ax1 = ax.flatten()

# Preparing data for plotting smooth function
# Creating list with numpy method 'arange'
x0 = np.arange(1, 30, 0.1)
y0 = f_array(x0)

# Plotting smooth function in range [1, 30]
# Giving title to the figure and axises
ax0.set_title('Smooth function f(x)')
ax0.set_xlabel('x')
ax0.set_ylabel('y')
# Showing dashed lines to the found minimums
# By defining 'ymax' or 'xmax' we limit the end of the lines
# 'ymax' or 'xmax' can be in range between 0 and 1
ax0.axvline(x=4.1362, ymax=0.85, color='c', linestyle='--', linewidth=0.8)
ax0.axhline(y=1.7452, xmax=0.14, color='c', linestyle='--', linewidth=0.8)
ax0.axvline(x=25.8801, ymax=0.05, color='r', linestyle='--', linewidth=0.8)
ax0.axhline(y=-11.8988, xmax=0.83, color='r', linestyle='--', linewidth=0.8)
# Another way to draw the limited line is as following:
# ax0.plot(np.arange(1, 10, 2), np.array([2]*5))  # arrays fo axises 'x' and 'y' has to have the same dimensions
# Creating the figure for smooth function
ax0.plot(x0, y0, 'b', 4.1362, 1.7452, 'co', 25.8801, -11.8988, 'ro')


# Preparing data for plotting non-smooth function
# Creating list with numpy method 'arange'
x1 = np.arange(1, 30, 0.1)
y1 = h_array(x1)

# Plotting non-smooth function in range [1, 30]
# Giving title to the figure and axises
ax1.set_title('Non-smooth function h(int(f(x)))')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
# Showing dashed lines to the found minimum
# By defining 'ymax' or 'xmax' we limit the end of the lines
# 'ymax' or 'xmax' can be in range between 0 and 1
ax1.axvline(x=25.0463, ymax=0.05, color='r', linestyle='--', linewidth=0.8)
ax1.axhline(y=-11, xmax=0.85, color='r', linestyle='--', linewidth=0.8)
ax1.axvline(x=30, ymax=0.43, color='c', linestyle='--', linewidth=0.8)
ax1.axhline(y=-5, xmax=0.95, color='c', linestyle='--', linewidth=0.8)
# Another way to draw the limited line is as following:
# ax0.plot(np.arange(1, 10, 2), np.array([2]*5))  # arrays fo axises 'x' and 'y' has to have the same dimensions
# Creating the figure for non-smooth function
ax1.plot(x1, y1, 'b', 30, -5, 'co', 25.0463, -11.0, 'ro')


# Function to make distance between figures
plt.tight_layout()
# Giving the name to the window with figures
figure.canvas.set_window_title('Smooth and non-smooth functions to be optimized')
# Showing result
plt.show()
