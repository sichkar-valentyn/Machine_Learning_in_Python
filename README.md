# Machine Learning in Python
Implementing Machine Learning algorithms and techniques in Python.

### Reference to:
Valentyn N Sichkar. Machine Learning in Python // GitHub platform

## Description
Practical experiments on Machine Learning in Python.

## Content
Codes (it'll send you to appropriate file):
* [Processing_Sentences](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Processing_Sentences.py)
* [Function_approximation](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Function_approximation.py)

<br/>
Experimental results (figures and tables on this page):

* <a href="#Processing sentences and finding cosine distances">Processing sentences and finding cosine distances</a>
* <a href="#Approximation of functions via linear equations">Approximation of functions via linear equations</a>

### <a name="Processing sentences and finding cosine distances">Processing sentences and finding cosine distances</a>
Implementing the task about processing sentences. Finding cosine distance between first sentence and all others. For implementation a two-dimensional matrix is created, where rows are sentences (objects) and columns are words (properties).
<br/>Matrix is filled with numbers that corresponds to number of times every word (property) were met in every sentence. Then, after matrix was built, distances are calculated between first vector (row) and all others. Calculation is done with the help of **'scipy.spatial.distance.cosine'** function.
<br/><br/>Code is shown below with a lot of comments:

```py
import re
import numpy as np
from scipy.spatial.distance import cosine


# Reading the file with sentences
# Writing lines into the list
# In this case we create list right when we read lines with function 'readlines()'
with open('sentences.txt', 'r') as f:
    lst = f.readlines()

# Putting all letters in the list to lowercase
for i in range(len(lst)):
    lst[i] = lst[i].lower().strip()  # Also, deleting sign '\n' at the end of every sentence

# Going through all lines in the list and splitting them into the words
# Using regular expression with pattern '[^a-z]' to split lines with
# Writing all unique words to the dictionary
lst_words = []  # Temporary list for separating words in every sentence
k = 0  # Variable for keys in dictionary
d = {}
for x in lst:
    lst_words += re.split('[^a-z]', x)
    for y in lst_words:
        # Checking if word is already in the dictionary
        if y != '' and (y not in d.values()):
            d[k] = y
            k += 1

# Creating matrix NxM for further calculations
# Where n - is number of sentences (lines in the list)
# And m - is total amount of unique words (length of the set)
a = np.zeros((len(lst), len(d)))  # (22, 254)

# Going through all lines (sentences) of the list
# Calculating how many times every unique word is included into every sentence
# Writing results into the matrix 'a'
number_of_words = 0
for i in range(len(lst)):
    # By expression 're.split('[^a-z]', lst[i])' we create list of words from every sentence
    words_in_sentence = list(filter(None, re.split('[^a-z]', lst[i])))
    number_of_words += len(words_in_sentence)
    print(words_in_sentence)
    for j in range(len(d)):
        # Then we compare each element of this list (each word) with each word in the dictionary
        a[i, j] = int(words_in_sentence.count(d[j]))

# Sum of all weights in matrix 'a' has to be equal to number of words in all sentences
print(a.sum())  # 484
print(number_of_words)  # 484
# One more way to calculate all number of words in all sentences
all_words = list(filter(None, re.split('[^a-z]', str(lst))))
print(len(all_words))  # 484

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

print(result_1, result_2)  # sentences number 6 and 4
print(d)

```

As a result we get dictionary with numner of sentence as a key (from the 1st one) and distance to the very first sentence (0 one):
{1: 0.9527544408738466, 2: 0.8644738145642124, 3: 0.8951715163278082, 4: 0.7770887149698589, 5: 0.9402385695332803, 6: 0.7327387580875756, 7: 0.9258750683338899, 8: 0.8842724875284311, 9: 0.9055088817476932, 10: 0.8328165362273942, 11: 0.8804771390665607, 12: 0.8396432548525454, 13: 0.8703592552895671, 14: 0.8740118423302576, 15: 0.9442721787424647, 16: 0.8406361854220809, 17: 0.956644501523794, 18: 0.9442721787424647, 19: 0.8885443574849294, 20: 0.8427572744917122, 21: 0.8250364469440588}

Full code is available here: [Processing_Sentences.py](https://github.com/sichkar-valentyn/Machine_Learning_in_Python/tree/master/Processing_Sentences.py)

### <a name="Approximation of functions via linear equations">Approximation of functions via linear equations</a>

![RGB_channels](images/RGB_channels.png)

<br/>

### MIT License
### Copyright (c) 2018 Valentyn N Sichkar
### github.com/sichkar-valentyn
### Reference to:
Valentyn N Sichkar. Machine Learning in Python // GitHub platform
