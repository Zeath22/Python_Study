from array import array
# we use arrays only if we have a very large dataset or list
# it has better performance
# arrays can store one type at a time
# and we have identify which type we're gonna have
# Search for python typecode
numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0      this will give an error because its float
