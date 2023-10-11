# Internet WAY
sentence = "This is a common interview question"
holder = [*sentence]
most = max(holder, key=holder.count)
print(most)

######################################################
# My WAY
from pprint import pprint  # nopep8
dictOfChars = {}
for x in sentence:
    if dictOfChars.get(x) == None:
        dictOfChars[x] = 1
    else:
        dictOfChars[x] += 1
pprint(dictOfChars)
print(max(dictOfChars, key=dictOfChars.get))

##################################################
# His WAY
dictOfChars = {}
for x in sentence:
    if x in dictOfChars:
        dictOfChars[x] += 1
    else:
        dictOfChars[x] = 1

# this sorts them by their key values
# we make them into tuples by .items()
# and we reverse them
frequency_Sorted = sorted(dictOfChars.items(),
                          key=lambda TheKV: TheKV[1],
                          reverse=True)
print(frequency_Sorted[0])
