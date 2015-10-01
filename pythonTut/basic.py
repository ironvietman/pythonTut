print "Hello World" # Note that print is a statment

### Working with Literal Constants
## Numbers
# ints and floats
# There is no separate long type.  The int type can be an integer of any size.

## Strings
# You can use single quotes and double quotes freely within the triple quotes
# Single and double quotes are the same.
# There is no separate char data type in Python.  There is no real need for it
# and I am sure you won’t miss it.
print '''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

## Format method
# better than string concatenation
age = 20
name = 'Swaroop'

print '{0} was {1} years old when he wrote this book'.format(name, age)
print 'Why is {0} playing with that python?'.format(name)

print name + ' is ' + str(age) + ' years old'

# decimal (.) precision of 3 for float '0.333'
print '{0:.3f}'.format(1.0/3)
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print '{0:_^11}'.format('hello')
# keyword-based 'Swaroop wrote A Byte of Python'
print '{name2} wrote {book}'.format(name2='Swaroop',
                                   book='A Byte of Python')

# stay on the same line with a comma
print 'a',
print 'b'

## Raw Strings
# If you need to specify some strings where no special processing such as escape
# sequences are handled, then what you need is to specify a raw string by prefixing
# r or R to the string. An example is

print r"Newlines are indicated by \n"

# Always use raw strings when dealing with regular expressions. Otherwise, a
# lot of backwhacking may be required.

### Variables
# Python is strongly object-oriented in the sense that everything is an object
# including numbers, strings and functions

# Variables are used by just assigning them a value. No declaration or
# data type definition is needed/used.

### Tips
# use the \ on a long line of code. it breaks it into multiple physical lines

# no need for semicolons unless you have more than one logical line on a single physical line
# Not Recommended

# None is a special type in Python that represents nothingness. For example, it is used to
# indicate that a variable has no value if it has a value of None.

### Operators
print 5+1 #add
print 5-1 #subtract
print 5*1 #mult
print 5**5 #power
print 'la' *3 # Repeating strings with multiply

length = 5
breadth = 2
area = length * breadth
print 'Area is', area
print 'Perimeter is', 2 * (length + breadth)