# Data Structures Excercise
from pprint import pprint

# find the most repeated letter in the sentence
sentence = "this is a common interview question"

# Define open dictionary
char_frequency = {}

# loop over the string in sentence variable
for char in sentence:
    # define a key in dictionary for each charachter
    # add counting value if already available in the dictionary
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# creating a sorted list out of the dictionary
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)

# print sorted list (Pretty print function was imported to present the list properly)
pprint(char_frequency_sorted, width=10,)

# print the first item in the list
print([char_frequency_sorted[0]])
