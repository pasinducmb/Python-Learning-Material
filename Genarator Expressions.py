# Generator Expressions
from sys import getsizeof

# Comprehension for Lists and Tuples

value = [(x + 1)**2 for x in range(10)]
print("List: ", value)

value = ((x + 1)**2 for x in range(10))
print("Tuple: ", value)

# (reason for error is due to tuples are not coprehendible objects as Lists, sets and dictionaries, therefore generator objects)
# Use Case: when infinite number of data is present which could take more memory for operating

# Comprehension for Tuples (defining generator objects)
value = ((x + 1)**2 for x in range(10))

for x in value:
    print("Gen: ", x)

# Size Comparison between Lists and Gen Objects
value = ((x + 1)**2 for x in range(1000000))
print("Gen Size:", getsizeof(value), "Bytes")

value = [(x + 1)**2 for x in range(1000000)]
print("List Size:", getsizeof(value), "Bytes")
