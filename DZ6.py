# Task 1
class Rectangle:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        area = self.width * self.heigth
        return area

    def perimeter(self):
        perimeter = (self.width + self.heigth) * 2
        return perimeter

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

rect = Rectangle(4, 5)
print(f'Периметр прямоугольника: {rect.perimeter()}')
print(f'Площадь прямоугольника: {rect.area()}')

sq = Square(3)
print(f'Периметр квадрата: {sq.perimeter()}')
print(f'Площадь квадрата: {sq.area()}')

# Task 2

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f'Name: {self.name} | Age: {self.age} | Gender: {self.gender}')

person = Person('Alina', 27, 'Female')
person.introduce()

class Employee(Person):

    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

    def work(self):
        print(f'Name: {self.name} | Salary: {self.salary} | Position: {self.position}')

employee = Employee('Tanny', 25, 'Female', 83000, 'Technical support employee')
employee.introduce()
employee.work()