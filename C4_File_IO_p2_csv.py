# if we want save multiple info for line we use comma seperated values .csv file
with open("Names_age.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is {row[1]} years old")
        # or we can do it this way, less complex
        name, age = line.rstrip().split(",")
        print(f"{name} is {age} years old")
