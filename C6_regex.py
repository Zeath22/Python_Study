import re

# the strip will remove any space characters if user inputed it
email = input("email: ").strip()

# we use search function from re that takes 3 arguments or less (patern, string, flags=0)
# we tell the function what patern to follow for the string that we provide
# .     any character except a newline
# *     0 or more repetitions
# +     1 or more repetitions
# ?     0 or 1 repetition
# {m}   m repetitions
# {m-n} m-n repetitions
# ^     indicating the start of the string
# $     indicating the end of the string
# []    set of characters
# [^]   anything except these charaters
# \ for any character to be taken raw like the dot(.) we need to include the r before the string
if re.search(r"^.+@.+\.com$", email):
    print("1st test: valid email")
else:
    print("1st test: invalid email!")

# we are updating the regex
# this regex prevents spaces and other @ signs like (hello z@n @ gm@il.com)
if re.search(r"^[^@ ]+@[^@ ]+\.com$", email):
    print("2nd test: valid email")
else:
    print("2nd test: invalid email!")


# we are updating the regex
# this regex allows alpha numeric characters (alphabet and numbers) and underscores
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("3rd test: valid email")
else:
    print("3rd test: invalid email!")


# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \s    not a whitespace character
# \w    word characters + numbers + underscore
# \W    not a word character

# we are updating the regex
# this regex allows alpha numeric characters but we only write \w which means word charaters
if re.search(r"^\w+@\w+\.com$", email):
    print("4th test: valid email")
else:
    print("4th test: invalid email!")

# A|B   either a or b
# (..)  a selected group
# (?:..) not capturing groups
# we are updating the regex
# this regex allows (.com .net .edu)
if re.search(r"^\w+@\w+\.(com|net|gov|edu)$", email):
    print("5th test: valid email")
else:
    print("5th test: invalid email!")

# we are updating the regex
# this regex allows to have dots in the username and it allows sub domains
# after the @ sign we added (\w+\.)* will allow 0 or more sub-domains
if re.search(r"^(\w|\.)+@(\w+\.)*\w+\.(com|net|gov|edu)$", email):
    print("6th test: valid email")
else:
    print("6th test: invalid email!")
