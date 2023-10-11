#################################################################
userInput = "241"
dict1 = {
    "1": "one",
    "2": "two",
    "3": "three"
}
output = ''

# if the get method doesn't find the key, By default it will put None
print(dict1.get(4))

for i in userInput:
    # if the get method doesn't find the key, By default it will put ! instead
    output += dict1.get(i, '!') + " "
print(output)
##################################################################
# Some useful methods of the dict class
print(dict1.keys())
print(dict1.values())

##################################################################
userInput2nd = "Good Morning :)"
words = userInput2nd.split(" ")
# dict2 = {
#     ":)": "😀",
#     ":(": "😔"
# }
dict2 = {
    ":)": ":')",
    ":(": ":'("
}
output2 = ""
for word in words:
    output2 += dict2.get(word, word) + " "
print(output2)

#################################################################
