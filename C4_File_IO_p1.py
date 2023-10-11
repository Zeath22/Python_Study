name = input("whats your name?")

# # we use open to open or create a file if it doesnt exist
# # the 2nd argument prepares it for w=write or r=read or a=appened etc
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# # close basically saves the file
# file.close()


# in a more pythonic way We want to automate the opening and closing by using with
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# if we want sort them then we need to read all of them to put them in memory by using a list
names_List = []
# if we dont specify the 2nd argument of the open then by default it will be read
with open("names.txt") as file:
    for name in file:
        # it prints 2 lines because of the previous \n that we used
        # we cant use end="" because append doesnt take keyword arguments
        names_List.append(name.rstrip())

for name in sorted(names_List):
    print(f"hello, {name}")
