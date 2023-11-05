# functions
#1. inbuilt function(int,str,bool,etc)
#2. module function(when related functions or related variables stored in same file)
# example math module
import math
print(dir(math))
# it will print all math function
# but if we want any particular function, then write

from math import sqrt
print(sqrt(4))

# if we want all function then
from math import*
print(sqrt(4))

