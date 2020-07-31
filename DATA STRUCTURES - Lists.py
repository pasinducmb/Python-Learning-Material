# DATA STRUCTURES - LISTS

# importing deque class from collections module
from collections import deque

# Defining the list
shopping_list = [
    ["item1", 20],
    ["item2", 15],
    ["item3", 10],
    ["item4", 5],
    ["item5", 12]
]
print(shopping_list)

# Sorting Items (decending order)

shopping_list.sort(key=lambda item: item[1], reverse=True)
print(shopping_list)

# Mapping Prices of the Shopping list to seperate list - Method 1

prices1 = list(map(lambda items: items[1], shopping_list))
print(prices1)


# Mapping Prices of the Shopping list to seperate list - Method 2

prices2 = [item[1] for item in shopping_list]
print(prices2)

# filtering shopping list - Method 1

filtered1 = list(filter(lambda items: items[1] >= 10, shopping_list))
print(filtered1)

# filtering shopping list - Method 2

filtered2 = [item for item in shopping_list if item[1] >= 10]
print(filtered2)


# Combining two lists (Zip Function)

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list(zip(list1, list2)))


# Stacking Items to list(LIFO)
shopping_list.append(["Product 6", 30])
print(shopping_list)

# Removing last item
last = shopping_list.pop()
print(last)
print(shopping_list)

# Redirecting to last item remaining
print("Redirecting to Item", shopping_list[-1])

# Diabling the redirect if the list is empty
if not shopping_list:
    print("Redirecting Disabled")
else:
    print("Redirecting to Item", shopping_list[-1])

# Queue the Items in list

ticked_off_shopping_list = deque(shopping_list)
ticked_off_shopping_list.popleft()
print(ticked_off_shopping_list)

if not ticked_off_shopping_list:
    print("Empty")
