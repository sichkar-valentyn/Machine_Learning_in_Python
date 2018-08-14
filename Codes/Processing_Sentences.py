# Implementing the task about sentences
# Finding cosine distance between first sentence and all others
# For implementation a matrix NxM is created
# Where N is number of sentences (objects)
# And M is number of words (properties)
# Matrix is filled with numbers that corresponds to number of times each word (property) were met in each sentence
# After matrix was built, distances are calculated between first vector (row) and all others
# Calculation is done with the help of 'scipy.spatial.distance.cosine' function


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
