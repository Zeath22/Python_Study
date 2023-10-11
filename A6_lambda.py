# This is one way do to it, not a good looking one
# def sort_item(item):
#     return item[1]


# # we dont call the function but we pass it's name as a reference key on how to sort each item
# items.sort(key=sort_item)
# print(items)

# A lambda function is a small anonymous function.
# It can take any number of arguments, but can only have one expression.
# lambda arguments : expression
# normal fuunction
def add(a, b):
    return a+b


print(add(4, 5))

# lambda function
x = (lambda x, y: x+y)      # nopep8
print(x(4, 6))              # nopep8

# we can also use it like this
print((lambda x, y: x+y)(4, 6))


#########################################
# another way to use lambdas is with (maps)
items = [
    ("item1", 10),
    ("item2", 9),
    ("item3", 12)
]

# instead of this
# prices = []
# for item in items:
#     prices.append(item[1])

# we use a map which takes a function like (lambda) and an iterable like (list)
mapped = map(lambda item: item[1], items)
print(mapped)        # this is an iterable
print(list(mapped))  # this puts it in a list

##########################################
# we also have the (filter function)
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


###########################################
# only in python we have (list comprehensions)
# if we put them in a square bracket its a list, if in curlys then dictionaries
mapped = list(map(lambda item: item[1], items))         # these 2 are the same                  # nopep8
mapped = [item[1] for item in items]                    # but list comprehensions are prefered  # nopep8

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
