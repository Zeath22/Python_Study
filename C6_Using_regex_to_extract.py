import re

url = input("name: ").strip()

# In this regex we are trying to extract the username(data) matching a specific description
# we first use the ^ to say it starts from here
# the s optional
# www. is not a capturing group that returns to matches and its optional
# then the username could be alpha numeric and it's getting captured
matches = re.search(
    r"^https?//:(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE)

if matches:
    print(f"USername: {matches.group(1)}")
