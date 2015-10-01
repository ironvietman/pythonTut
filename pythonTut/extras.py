### Lambda expression
# A lambda statement is used to create new function objects.  Essentially, the
# lambda takes a parameter followed by a single expression only which becomes
# the body of the function and the value of this expression is returned by the
# new function.

points = [ { 'x' : 2, 'y' : 3 },
           { 'x' : 6, 'y' : 1 } ]
points.sort(key=lambda i : i['y']) # The function is i['y'] meaning we want to sort on values of y
print points
points.sort(key=lambda i : i['y'] +i['x']) # The function is i['y'] meaning we want to sort on sum of values
print points


## Special Methods 
# There are certain methods such as the init and del methods
# which have special significance in classes.
#init(self, �?) 
#This method is called just before the newly created object is returned for usage.

#del(self) 
#Called just before the object is destroyed (which has unpredictable timing, so avoid using this)

#str(self) 
#Called when we use the print statement or when str() is used.

#lt(self, other) 
#Called when the less than operator (<) is used. Similarly, there are special methods for all the operators (+, >, etc.)

#getitem(self, key) 
#Called when x[key] indexing operation is used.

#len(self) 
#Called when the built-in len() function is used for the sequence object.


class Person:
    def __init__(self, name):
        self.name = name
    def __getitem__(self,key):
        if key == "name": return self.name
    def __len__(self):
        print "HAHA"
        return 0

person = Person("Robert")
print person["name"]
len(person)

## Passing tuples around
def returning_tuples():
    return (1, 3, 4 ,"words")

num1, num2, num3, words = returning_tuples();
print words

# using this to swap values
a = 5; b = 8
a,b = b,a
print a,b

### List Comprehension
# List comprehensions are used to derive a new list from an existing list
listone = [1, 2, 3, 4]
listtwo = [2*i for i in listone if i >= 2] #manipulation, values from list, condition
print listtwo

### assert statement
# The assert statement is used to assert that something is true The assert
# statement should be used judiciously.  Most of the time, it is better to
# catch exceptions, either handle the problem or display an error message to
# the user and then quit.
mylist = ['item0']
assert len(mylist) >= 1
mylist.pop()
# assert len(mylist) >= 1 ### WILL BREAK

### Decorators
# Decorators are a shortcut to applying wrapper functions.  This is helpful to
# "wrap" functionality with the same code over and over again.  

# a decorator receives the method it's wrapping as a variable 'f'
def increment(f):
    # we use arbitrary args and keywords to
    # ensure we grab all the input arguments.
    def wrapped_f(*args, **kw):
        # note we call f against the variables passed into the wrapper,
        # and cast the result to an int and increment .
        return int(f(*args, **kw)) + 1
    return wrapped_f  # the wrapped function gets returned.

@increment
def plus(a, b):
    return a + b

result = plus(4, 6)
print result