# if we want to unpack * a list or a string or anything

numbers = [1, 2, 3]
print(*numbers)

numbers2 = list(range(3))
print(*numbers2)

numbers3 = [*range(3)]
print(numbers3)

values = [*range(3,), *"--"]
print(values)

valuesCombined = [*values, *numbers2]
print(valuesCombined)

dict1 = {"x": 1}
dict2 = {"x": 10, "y": 20}
combined = {**dict1, **dict2, "z": 30}
print(combined)
# if there are same key names, the latest one will replace the older
