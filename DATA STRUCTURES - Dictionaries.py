# DATA STRUCTURES - DICTIONARIES

# Defining a Dictionary
phonebook = dict(pasiya=111111, sameera=222222, bhashi=333333)
print(phonebook)

# Checking for a key value pair
# Method 1
if "dilu" in phonebook:
    print("Yes")
else:
    print(0)

# Method 2
print(phonebook.get("dilu", 0))

# Adding Key value pair

phonebook["dilu"] = 444444
print(phonebook)

# Deleting Key value pair
del phonebook["dilu"]
print(phonebook)

# looping over items

# Method 1
print("Method 1")
for a in phonebook:
    print(a, phonebook[a])

# Method 2
print("Method 2")
for a, b in phonebook.items():
    print(a, b)

# List Comprehension vs Dictrionary Comprehension

# List comprehension (vairable = [expression for item in items])

list_comprehension_1 = [x*2 for x in range(5)]
print(list_comprehension_1)

# Dictionaries Comprehension (variable = {key:value (i.e. expression) for item in items})
dictionary_comprehension = {x: x*2 for x in range(5)}
print(dictionary_comprehension)
