print("fe")
xx = 1
a = "apple"
print(a[1:-2])

print('h' * 8)

name = 'zan'
print(f'hi my name is {name}')

message = "hello how are you?"
newMessage = message.replace('hello', 'hey')
print(newMessage)

contains = 'hey' in newMessage
print('hey' in newMessage)

if 'hi' in newMessage:
    print('not quite right')
elif 'hey' in newMessage:
    print('righto')
else:
    print('this should be fixed')

knockAtDoor = 0
while knockAtDoor < 3:
    print('no answer')
    knockAtDoor += 1
    if knockAtDoor == 3:
        print('leave')

list1 = [1, 2, 3, 4, 5]
list1.append(4)
list1.sort()
list1.pop()
list1.insert(1, 6)
list1.insert(1, 8)
print(list1)

cordinates = (1, 3, 4)
x, y, z = cordinates
print(y)

F = [6, 2, 6, 2, 2]
for item in F:
    for x in range(item):
        print('x', end='')
    print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])
