print("Question 1")
# 1.
# Create methods for the "Calculator" class that can do the following:
#     Add two numbers.
#     Subtract two numbers.
#     Multiply two numbers.
#     Divide two numbers.

# Examples
#   calculator = Calculator()
#   calculator.add(10, 5) ➞ 15
#   calculator.subtract(10, 5) ➞ 5
#   calculator.multiply(10, 5) ➞ 50
#   calculator.divide(10, 5) ➞ 2

class Calculator:

    # def addnew(self,n1,n2):
    #     return n1+n2

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        return(self.n1 + self.n2)

    def subtract(self):
        return(self.n1 - self.n2)
    
    def multiply(self):
        return(self.n1 * self.n2)

    def divide(self):
        return(self.n1 / self.n2)

example = Calculator(10, 5)
print(example.add())
print(example.subtract())
print(example.multiply())
print(example.divide())
# print(example.addnew(2,3))

print("Question 2")

# 2.
# Create a method in the "Person" class which returns how another person's age compares. 
# Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, 
# return a sentence in the following format:
#   {other_person} is {older than / younger than / the same age as} me.

# Examples
#   p1 = Person("Samuel", 24)
#   p2 = Person("Joel", 36)
#   p3 = Person("Lily", 24)
#   p1.compare_age(p2) ➞ "Joel is older than me."
#   p2.compare_age(p1) ➞ "Samuel is younger than me."
#   p1.compare_age(p3) ➞ "Lily is the same age as me."

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def compare_age(self,other_person):
        if self.age > other_person.age:
            print("{} is younger than me.".format(other_person.name))
        
        elif self.age == other_person.age:
            print("{} is the same age as me.".format(other_person.name))

        else:
            print("{} is older than me.".format(other_person.name))

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

p1.compare_age(p2)
p2.compare_age(p1) 
p1.compare_age(p3) 

print("Question 3")

# 3.
# Your task is to create a "Circle" constructor that creates a circle with a radius provided by an argument.
#  The circles constructed must have two getters "getArea()" and "getPerimeter()" 
# which give both respective areas and perimeter (circumference).

# Examples
#   circy = Circle(11)
#   circy.getArea()
#     # Should return 380.132711084365

#   circy = Circle(4.44)
#   circy.getPerimeter()
#     # Should return 27.897342763877365

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.141592653589793

    def getArea(self):
        print(self.radius ** 2 * self.pi)
    
    def getPerimeter(self):
        print(self.radius * 2 * self.pi)

circy = Circle(11)
circy.getArea()
circy.getPerimeter()


