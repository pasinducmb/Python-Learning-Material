# Unpacking Operator

# Unpacking a list using unpack operator i.e. *
list_packed = [1, 2, 3, 4, 5]
print(list_packed)
print(*list_packed)

# defining an unpacked list via Unpack Operator i.e. *
values = [*range(5), *"Hello"]
print(values)

# combining two or more lists with unpack operator
first = [1, 2, 3]
second = [4, 5, 6]

# without unpack operator
combined = [first, second]
print(combined)

# with unpack operator
combined = [*first, *second]
print(combined)


# combining two or more dictionaries with unpack operator i.e. **

# without ** Operator
first_dict1 = dict(a=1, b=2, c=3)
second_dict1 = dict(x=4, y=5, z=6)
combined_dict1 = (first_dict1, second_dict1)
print(combined_dict1)

# with ** Operator
first_dict2 = dict(a=1, b=2, c=3)
second_dict2 = dict(x=4, y=5, z=6)
combined_dict2 = {**first_dict2, **second_dict2}
print(combined_dict2)
