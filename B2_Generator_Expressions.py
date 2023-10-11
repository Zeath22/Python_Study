# We've learned about list comprehensions in lambdas
# but if we use it for tuples it becomes a generator expression
# they dont store every value in memory like list
# they generate a new value with each iteration

values = (x*2 for x in range(5))
print("this is a ", values)
for x in values:
    print(x)

####################################
# we can check how many bytes these take
# the generator expression always takes 208 even if its 10000000
# but the list changes
from sys import getsizeof  # nopep8

values2 = (x*2 for x in range(1000))
values3 = [x*2 for x in range(1000)]

print("1st gen expression:", getsizeof(values))
print("2st gen expression:", getsizeof(values2))
print("the list:", getsizeof(values3))
