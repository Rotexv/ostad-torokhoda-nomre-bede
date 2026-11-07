class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Zoo:
    def __init__(self, name, city, animals):
        self.name = name
        self.city = city
        self.animals = animals


class Student:
    def __init__(self, name, age, student_id, major):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


cat = Animal("Tom", "Cat", 3)
lion = Animal("Simba", "Lion", 5)
human = Human("Ali", 30, "male")
zoo = Zoo("Eram Zoo", "Tehran", [cat, lion])
student = Student("Soren", 20, "40012345", "Computer Engineering")
fraction = Fraction(3, 4)
city = City("Tehran", "Iran", 9000000)
car = Car("Toyota", "Corolla", 2020)
book = Book("Animal Farm", "George Orwell", 112)
phone = Phone("Samsung", "Galaxy A16", 800)

print("Animal:", cat.name, cat.species, cat.age)
print("Animal:", lion.name, lion.species, lion.age)
print("Human:", human.name, human.age, human.gender)
print("Zoo:", zoo.name, zoo.city, [a.name for a in zoo.animals])
print("Student:", student.name, student.age, student.student_id, student.major)
print("Fraction:", f"{fraction.numerator}/{fraction.denominator}")
print("City:", city.name, city.country, city.population)
print("Car:", car.brand, car.model, car.year)
print("Book:", book.title, book.author, book.pages)
print("Phone:", phone.brand, phone.model, phone.price)