## Classes
# Class methods have only one specific difference from ordinary functions.This
# particular variable refers to the object itself, and by convention, it is
# given the name self.  The self in Python is equivalent to the this pointer in
# C++ and the this reference in Java and C#.

# All class members (including the data members) are public and all the methods
# are virtual in Python.

# All class members are public.  One exception: If you use data members with
# names using the double underscore prefix such as __privatevar

# the convention followed is that any variable that is to be used only within
# the class or object should begin with an underscore and all other names are
# public and can be used by other classes/objects

class Person:
    pass # An empty block

p = Person()
print(p)

class Person2:
    def __init__(self, name): #run as soon as an object of a class is instantiated
        self.name = name
    def say_hi(self):
        print 'Hello, my name is',self.name

p2 = Person2("Robert")
p2.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    # Also note that an object variable with the same 
    # name as a class variable will hide the class variable!
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print "(Initializing {})".format(self.name)

        # When this person is created, the robot
        # adds to the population
        # could have also used self.__class__.population 
        Robot.population += 1

    def die(self):
        """I am dying."""
        print "{} is being destroyed!".format(self.name)

        Robot.population -= 1

        if Robot.population == 0:
            print "{} was the last one.".format(self.name)
        else:
            print "There are still {:d} robots working.".format(
                Robot.population)

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print "Greetings, my masters call me {}.".format(self.name)

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print "We have {:d} robots.".format(cls.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do some work here.\n"

print "Robots have finished their work. So let's destroy them."
droid1.die()
droid2.die()

Robot.how_many()

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        '''Tell my details.'''
        print 'Name:"{}" Age:"{}"'.format(self.name, self.age),

class Teacher(SchoolMember): #inheritance
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        #Python does not automatically call the constructor of the base class,
        #you have to explicitly call it yourself
        SchoolMember.__init__(self, name, age) 
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tellmore(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)

    def tellmore(self):
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
    #Python always starts looking for methods in the actual type first then
    #starts looking at the methods belonging to its base classes one by one in
    #the order they are specified in the tuple in the class definition
    member.tellmore()