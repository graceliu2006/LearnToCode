print("Question 1")

# 1.
# Create the instance attributes fullname and email in the Employee class. 
# Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, 
# separated by a space.
# Form the email by joining the first and last name together with 
# a . in between, and follow it with @company.com at the end. 
# Make sure everything is in lowercase.

# Examples

# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary", "Sue")
# emp_3 = Employee("Antony", "Walker")

# emp_1.fullname ➞ "John Smith"
# emp_2.email ➞ "mary.sue@company.com"
# emp_3.firstname ➞ "Antony"

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def firstname(self):
        print(self.first)
    
    def lastname(self):
        print(self.last)

    def fullname(self):
        print(self.first + " " + self.last)
        

    def email(self):
        print(self.first.lower() + "." + self.last.lower() + "@company.com")
        


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")

emp_1.fullname()
emp_2.email() 
emp_3.firstname() 

print("Question 2")

# 2.
# Write a class called Name and create the following attributes 
# given a first name and last name (as fname and lname):
# An attribute called fullname which returns the first and last names.
# A attribute called initials which returns the first letters 
# of the first and last name. Put a . between the two letters.
# Remember to allow the attributes fname and lname to be accessed 
# individually as well.

# Examples
# a1 = Name("john", "SMITH")
# a1.fname ➞ "John"
# a1.lname ➞ "Smith"
# a1.fullname ➞ "John Smith"
# a1.initials ➞ "J.S"

class Name:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def fname(self):
        print(self.firstname)
    
    def lname(self):
        print(self.lastname)

    def fullname(self):
        print(self.firstname + " " + self.lastname)   

    def initials(self):
        finitial = self.firstname[0]
        linitial = self.lastname[0]
        print(finitial.upper() + "." + linitial.upper() + ".")

a1 = Name("john", "SMITH")
a1.fname()
a1.lname() 
a1.fullname() 
a1.initials() 

print('Question 3')
# 3.
# Count Number of Instances
# Create a class named User and create a way to check the number of users 
# (number of instances) that were created, so that the value can be accessed as a class attribute.

# Examples
# u1 = User("johnsmith10")
# User.user_count ➞ 1

# u2 = User("marysue1989")
# User.user_count ➞ 2

# u3 = User("milan_rodrick")
# User.user_count ➞ 3

# Make sure that the usernames are accessible via the instance attribute username.
# u1.username ➞ "johnsmith10"
# u2.username ➞ "marysue1989"
# u3.username ➞ "milan_rodrick"

# Hint
# http://www.learningaboutelectronics.com/Articles/How-to-count-the-number-of-objects-in-a-class-in-Python.php

class User:
    number_created = 0
    
    def __init__(self, newuser):
        self.newuser = newuser
        User.number_created += 1

    def user_count():
        print(User.number_created)

    def username(self):
        print(self.newuser)

u1 = User("johnsmith10")
User.user_count()

u2 = User("marysue1989")
User.user_count()

u3 = User("milan_rodrick")
User.user_count()

u1.username() 
u2.username()
u3.username()

print("Question 4")

# 4.
# Create a Person class which will have three properties:
# Name
# List of foods they like
# List of foods they hate

# In this class, create the method taste():
# It will take in a food name as a string.
# Return {person_name} eats the {food_name}.
# If the food is in the person's like list, add 'and loves it!' to the end.
# If it is in the person's hate list, add 'and hates it!' to the end.
# If it is in neither list, simply add an exclamation mark to the end.

# Examples
# p1 = Person("Sam", ["ice cream"], ["carrots"])
# p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
# p1.taste("cheese") ➞ "Sam eats the cheese!"
# p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

# Notes
# A person can have an empty list for foods they hate and/or love.
# Check the Resources for some helpful tutorials on Python classes.

class Person:

    def __init__(self, name, likelist, hatelist):
        self.name = name
        self.likelist = likelist
        self.hatelist = hatelist

    def taste(self, eaten):
        if eaten in self.likelist:
            print("{} eats the {} and likes it!".format(self.name, eaten))
        elif eaten in self.hatelist:
            print("{} eats the {} and hates it!".format(self.name, eaten))
        else:
            print("{} eats the {}!".format(self.name, eaten))

p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") 
p1.taste("cheese")
p1.taste("carrots") 