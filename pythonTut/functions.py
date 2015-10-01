### Functions
def say_hello():
    # block belonging to the function
    print 'hello world'
# End of function

say_hello() # call the function
say_hello() # call the function again

# Using global within a function will use variables outside of the function. Not Recommended
x = 50
def func():
    global x

    print 'x is', x
    x = 2
    print 'Changed global x to', x

func()
print 'Value of x is', x

# Keyword arguments
# we can use the name of the variable instead of the position to set values
def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)

# VarArgs parameters
# can be used to take in any number of parameters
# *param, then all the positional arguments from that 
# point till the end are collected as a tuple called 'param'.
# **param, then all the keyword arguments from that point till 
# the end are collected as a dictionary called 'param'

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print total(10, 1, 2, 3, vegetables=50, fruits=100)


### DocStrings
# There are descritions for your functions
# The convention followed for a docstring is a multi-line string where 
# the first line starts with a capital letter and ends with a dot. Then the 
# second line is blank followed by any detailed explanation starting from the 
# third line. You are strongly advised to follow this convention for all your 
# docstrings for all your non-trivial functions.
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print_max(3, 5)
print print_max.__doc__

