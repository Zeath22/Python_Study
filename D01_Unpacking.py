def total(gold, silver, bronze):
    # 10 bronze coins is a silver and 10 silver coins is a gold coin
    return (gold * 10 + silver) * 10 + bronze


# list unpacking
coins = [5, 10, 20]
# normally we wouldnt be able to pass a list into a function that wants ints
# but with the * star we can unpack it and not waste time
print(total(*coins), "bronze coins")

# dict unpacking
coins = {"gold": 5, "silver": 10, "bronze": 20}
#  ** star we can unpack it and not waste time
print(total(**coins), "bronze coins")
