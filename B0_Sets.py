# sets are like lists except values dont reaccure
# they are mostly used for mathematics

numbers = [1, 2, 3, 4]
first = set(numbers)
second = {1, 5}         # curly brackets indicates sets

print(first)
print(first | second)   # Union of first and second set
print(first & second)   # Intersection
print(first - second)   # difference
print(first ^ second)   # nopep8 # symmetric difference: when a value is in one of the sets but not in both

# doesn't support index
# print(first[0])   ERROR
if 1 in first:
    print("yes")
