# when we assign a to b, we are not creating a new variable
# we're just creating another refrence to the same point
a = [1]
b = a
b[0] = 0
if a[0] == b[0]:
    print(a[0])
    print(b[0])
    print("hello")

# if we want to have a seperate copy, we use
# b = a.copy()
