# conditioning lists
alpha = ["a", "b", "c", "d"]
reverse = alpha[::-1]
print(reverse)
goBy2 = alpha[::2]
print(goBy2)

#################################################
# Unpacking lists
numbers = [1, 2, 3]
first, second, third = numbers
print(first)
print(third)

# we should have the same amount of vars for the list, if not then its an error
# below this is wrong
# numbers = [1, 2, 3]
# first, second = numbers
# this gives an error

# but if you want some of the list then
numbers2 = [1, 2, 44, 6, 78, 73, 99]
first2, second2, *others = numbers2
print(first2)
print(others)

# first and last or Any other combo
first3, *others3, last3 = numbers2
print(first3, last3)
print(others3)


###########################################
# if we want to give our lists index then
# but this gives us tuples
alphabet = ["a", "b", "c"]
for letter in enumerate(alphabet):
    print(letter)

for index, letter in enumerate(alphabet):
    print(index, letter)


######################################
# adding and removing from a list
list1 = ["a", "b", "c", "d"]

# Add
list1.append('e')       # adding from the end
list1.insert(0, "-")    # adding from a specific index
print(list1)

# remove
list1.pop()             # removing from last
list1.pop(0)            # or remove a specific index
print(list1)

list1.remove("b")       # removes the first occurance of b
print(list1)

del list1[0:2]          # deleting a range of indexes
print(list1)

list1.clear()           # clear everything
print(list1)


##############################################
# sorting lists
numbers3 = [4, 1, 57, 3, 2, 67, 3]
print(sorted(numbers3))
print(sorted(numbers3, reverse=True))
print(numbers3)         # it doesnt modify the original

# 3
# but what if we had a list of tuples, sort them by prices
items = [
    ("item1", 10),
    ("item2", 7),
    ("item3", 13)
]


def sort_item(item):
    return item[1]


# we dont call the function but we pass it's name as a reference key on how to sort each item
items.sort(key=sort_item)
print(items)

# this not good looking way to do it So we use lambda, go to lambda


############################################################
# if we wanna take one item of each of our lists we use (Zip function)
list11 = [1, 2, 3]
list22 = [10, 20, 30]
zipped = list(zip(list11, list22))
print(zipped)
# or just put any iterable in there
print(list(zip("abc", list11, list22)))
# testing
print(list(zip("ab", list11, list22)))      # it will output the same amount every var has  # nopep8
print(list(zip("abc", zipped)))             # it will mix them                              # nopep8
