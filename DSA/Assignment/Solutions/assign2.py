
#Q1. Create a class Person with attributes name and age. Create a method show() to display the details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("Aashish", 21)
p.show()

#Q2. Create a class Circle with attributes radius. Create methods to set the radius, get the radius, calculate the area and circumference.
class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    def setradius(self, radius):
        self.radius = radius
    def getradius(self):
        return self.radius
    def getArea(self):
        return 3.14 * self.radius * self.radius
    def getCircumference(self):
        return 2 * 3.14 * self.radius

c = Circle()
c.setradius(7)
print("Radius:", c.getradius())
print("Area:", c.getArea())
print("Circumference:", c.getCircumference())

# Q3. Create a class Rectangle with attributes length and breadth. Create methods to set the dimensions, get the dimensions, calculate the area and perimeter.
class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth= 0
    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def showDimensions(self):
        return f"Length: {self.length}, Breadth: {self.breadth}"
    def area(self):
        return self.length * self.breadth

r = Rectangle()
r.setDimensions(10, 5)
r.showDimensions()
print("Area:", r.area())

#Q4. Create a class Book with attributes bookId, title and price. Create methods to set the details, get the details and display the details.
class Book:
    def __init__(self, bookId, title, price):
        self.bookId = bookId
        self.title = title
        self.price = price
    def show(self):
        print(f"Book ID: {self.bookId}, Title: {self.title}, Price: {self.price}")
b = Book(1, "Python", 100)
b.show()

#Q5. Create a class Team with attributes members. Create methods to add a member, remove a member and display the members.
class Team:
    def __init__(self):
        self.members = []
    def addMember(self, member):
        n = int(input("Enter number of team members: "))
        for i in range(n):
            name = input("Enter name of team member: ")
            self.members.append(name)
    def removeMember(self, member):
        self.members.remove(member)
    def showMembers(self):
        return self.members
t = Team()
t.addMember("Aashish")
print(t.showMembers())