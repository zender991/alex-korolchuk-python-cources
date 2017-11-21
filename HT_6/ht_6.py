'''Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з
2-ма числами, а саме додавання, віднімання, множення, ділення.
Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.'''


class Calc(object):             # create class Cald. Child of class object
    last_result = " "           # set empty value to attribute

    def add(self, first_value, second_value):       # create method. Arguments: self - instance, first_value,
                                                    # second_value - digits
        self.last_result = first_value + second_value       # result of adding write to initial instance attribute
        return self.last_result                             # return function result in instance attribute

    def subtract(self, first_value, second_value):          # methods below have the same logic like add method
        self.last_result = first_value - second_value
        return self.last_result

    def divide(self, first_value, second_value):
        self.last_result = first_value / second_value
        return self.last_result

    def multiply(self, first_value, second_value):
        self.last_result = first_value * second_value
        return self.last_result


a = Calc()              # create instance of class Calc
print(a.last_result)    # print last_result attribute after create instance
a.add(4, 5)             # execute add methods
print(a.last_result)    # print value of last_result attribute after method execution
a.subtract(45, 23)      # below the same logic
print(a.last_result)
a.divide(20, 6)
print(a.last_result)
a.multiply(3, 7)
print(a.last_result)


'''Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в
відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.'''


class Person(object):
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def show_age(self):
        return print("%s is %i years old" % (self.first_name, self.age))

    def print_name(self):
        return print("User's full name is %s %s" % (self.first_name, self.last_name))

    def show_all_information(self):
        return print("User's full information: First name - %s, Last name - %s, Age - %i, Gender - %s" %
                     (self.first_name, self.last_name, self.age, self.gender))


john = Person("John", "Smith", 43, "male")
sarah = Person("Sarah", "Connor", 56, "female")

john.show_age()
john.print_name()
john.show_all_information()
john.profession = "gg"
print(john.profession)


'''Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і
метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для
завдання початкових розмірів об'єктів при їх створенні.'''


class Figure(object):
    color = "white"

    def change_color(self, color):
        self.color = color
        return self.color


class Oval(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_square(self):
        oval_square = self.height * self.width * 3.1415
        return oval_square


class Square(Figure):

    def __init__(self, width):
        self.width = width

    def find_square(self):
        square_area = self.width ** 2
        return square_area


b = Oval(4, 5)
print(b.find_square())

c = Square(5)
print(c.find_square())
print(c.color)
c.change_color("red")
print(c.color)


'''Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.'''


class Figure2(object):

    def __init__(self, color):
        self.color = color

    def change_color2(self, color):
        self.color = color
        return self.color


class Oval2(Figure2):

    def __init__(self, width, height, color):
        Figure2.__init__(self, color)

        self.width = width
        self.height = height

    def find_square2(self):
        oval_square = "%s oval has square - %f" % (self.color, (self.height * self.width * 3.1415))
        return oval_square


class Square2(Figure2):

    def __init__(self, width, color):
        Figure2.__init__(self, color)

        self.width = width

    def find_square2(self):
        square_area = "%s square has area - %f" % (self.color, (self.width ** 2))
        return square_area


d = Oval2(5, 9, "blue")
print(d.find_square2())
e = Square2(6, "brown")
print(e.find_square2())
e.change_color2("black")
print(e.find_square2())


'''Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).'''


'''Напишіть програму в стилі ООП, що задовольняє наступним умовам: у програмі повинні бути два класи та два об'єкта,
що належать різним класам; один об'єкт за допомогою методу свого класу повинен так чи інакше змінювати дані
іншого об'єкта'''


'''Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.'''


class Example(object):

    instance_count = 0

    def __init__(self):
        Example.instance_count += 1

    def get_instance_count(self):
        return self.instance_count


example1 = Example()
example2 = Example()
example3 = Example()
print(example1.get_instance_count())


'''Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу. Виведіть типи зазначених
об'єктів. Створіть новий клас Thing2 і призначте йому атрибут letters зі значенням 'abc' . Виведіть на екран значення
атрибута letters. Створіть ще один клас Thing3 . Присвойте значення 'xyz' атрибуту об'єкта, який називається letters.
Виведіть на екран значення атрибута letters . '''


class Thing(object):
    pass


class Thing2(object):
    letters = "abc"


class Thing3(object):
    pass


example = Thing()
print(Thing.__class__)
print(example.__class__)

print(Thing2.letters)

Thing3.letters = "xyz"
print(Thing3.letters)


'''Створіть клас, який називається DefaultClass що має атрибути об'єкту name, symbol number . Виведіть атребути.'''

DefaultClass


