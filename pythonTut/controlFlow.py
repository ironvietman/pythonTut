### Control Flow
# Everything goes off intents. There are no brackets
# if statement

number = 23
guess = int(raw_input('Enter an integer : ')) # use int to convert string to integer

if guess == number:
    # New block starts here
    print 'Congratulations, you guessed it.'
    print '(but you do not win any prizes!)'
    # New block ends here
elif guess < number:
    # Another block
    print 'No, it is a little higher than that'
    # You can do whatever you want in a block ...
else:
    print 'No, it is a little lower than that'
    # you must have guessed > number to reach here

print 'Done'
# This last statement is always executed,
# after the if statement is executed.

# There is no switch statement in Python. You can use an if..elif..else statement to do 
# the same thing (and in some cases, use a dictionary to do it quickly) 


# while statement
running = True;
while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print 'No, it is a little higher than that.'
    else:
        print 'No, it is a little lower than that.'
else:
    # If there is an else clause for a while loop, 
    # it is always executed unless you break out of the loop with a break statement.
    print 'The while loop is over.'
    # Do anything else you want to do here

print 'Done'

# For Loop
for i in range(1, 5):
    print i
else:
    print 'The for loop is over'

# range is a built in function that returns  sequence of numbers an optional thrid input 
# is for step size
print range(1,5,2)

## Notes
# break and continue can be used within loops to leave early or continue
