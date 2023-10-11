# what we do normally
x = 1
y = 2

z = x
x = y
y = z
print(f"""
x = {x}
y = {y}  
""")

# what we can do by less code
x, y = y, x
print(f"""
x = {x}
y = {y}  
""")
