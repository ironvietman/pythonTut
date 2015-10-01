# Handling errors 
# We put all the statements that might raise exceptions/errors
# inside the try block and then put handlers for the appropriate
# errors/exceptions in the except clause/block

try:
    text = raw_input('Enter something --> ')
except EOFError:
    print 'Why did you do an EOF on me?'
except KeyboardInterrupt:
    print 'You cancelled the operation.'
else:
    print 'You entered {}'.format(text)


# Should be a class which directly or indirectly must be a derived class of the
# Exception class.
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = raw_input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print 'Why did you do an EOF on me?'
except ShortInputException as ex:
    print ('ShortInputException: The input was ' + \
           '{0} long, expected at least {1}')\
          .format(ex.length, ex.atleast)
else:
    print 'No exception was raised.'

import sys
import time

f = None
try:
    f = open("poem.txt")
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
        sys.stdout.flush() #so that it prints to the screen immediately
        print "Press ctrl+c now"
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print "Could not find file poem.txt"
except KeyboardInterrupt:
    print "!! You cancelled the reading from the file."
finally: #  before the program exits, the finally clause is executed 
    if f:
        f.close()
    print "(Cleaning up: Closed the file)"

# instead of doing the try and finally block,
# we can use with
with open("poem.txt") as f:
    for line in f:
        print line,