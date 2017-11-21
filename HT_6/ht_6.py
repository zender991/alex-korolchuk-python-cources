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
