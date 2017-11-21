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