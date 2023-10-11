import sys
# if we call our lib like this then we can avoid calling hello function
# like this C2_Custom_Lib.hello and can just call hello
# and we can avoid naming errors when we import other devs libraries
from C2_Custom_Lib import hello


# using sys argv allows us to use Command line Arguments
# we can pass arguments next to the python file name in terminal,
# the python name takes the 0 index in the arguments list
# so if we pass a name we can call it back by the 1 index
if len(sys.argv) == 2:
    hello(sys.argv[1])
