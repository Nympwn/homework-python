# Task 1
class Rectangle:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self, width, heigth):
        area = self.width * self.heigth
        return self.area

    def perimeter(self, width, heigth):
        perimeter = (self.width + self.heigth) * 2
        return self.perimeter

class Square(Rectangle):

    def __init__(self):
        self.side = []

# Task 2

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Name: {self.name} | Age: {self.age} | Gender: {self.gender}'

class Employee(Person):

    def __init__(self, salary, position):
        self.persons = []
        self.salary = salary
        self.position = position

    def work(self, salary, position):
        return f'Salary: {self.salary} | Position: {self.position}'