### Modules
# A module can be imported by another program to make use of its 
# functionality. This is how we can use the Python standard library as well
import sys

print('The command line arguments are:')
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

# Using from..import 
# this will avoid having to type the module name first
# Not Recommended
from math import sqrt
print "Square root of 16 is", sqrt(16)

## using the name attribute you can check if its imported or ran
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'

## Making your own Modules
import exampleMod

exampleMod.say_hi()
print 'Version',exampleMod.__version__
print 'Running as:', 
exampleMod.running_as()

## the dir function
# dir function to list the identifiers that an object defines. For example, 
# for a module, the identifiers include the functions, classes and variables 
# defined in that module.
print dir()
a = 5 # create variable a
print dir() # should see it here
del a # delete a so you cant use it anymore
print dir() # a is gone from here

## Packages
# These ar folders of modules with a special init.py
# The structure of a package could be something like the following
#- <some folder present in the sys.path>/
#    - world/
#        - __init__.py
#        - asia/
#            - __init__.py
#            - india/
#                - __init__.py
#                - foo.py
#        - africa/
#            - __init__.py
#            - madagascar/
#                - __init__.py
#                - bar.py