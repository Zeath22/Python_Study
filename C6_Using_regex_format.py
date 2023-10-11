import re

name = input("name: ").strip()
# if we're going to reformat a bunch of names or data but we might face user error
# we can use regex to reformat those data
# matches isn't only a boolean, it can capture groups matching in the string
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
