'''Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з
2-ма числами, а саме додавання, віднімання, множення, ділення.
Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
Результати записуються у файл.'''

class Calculator(object):

    def __init__(self):
        self.last_result = " "

    def add(self, a, b):
        result_list = []
        result_list.extend([a, " + ", b, " = ", a + b])
        return Calculator.write_to_file(result_list)

    def substract(self, a, b):
        result_list = []
        result_list.extend([a, " - ", b, " = ", a - b])
        return Calculator.write_to_file(result_list)

    def multiply(self, a, b):
        result_list = []
        result_list.extend([a, " * ", b, " = ", a * b])
        return Calculator.write_to_file(result_list)

    def divide(self, a, b):
        result_list = []
        result_list.extend([a, " / ", b, " = ", a / b])
        return Calculator.write_to_file(result_list)

    @staticmethod
    def write_to_file(result):
        with open('/python-cources/HT_7/results.txt', 'a') as myfile:  # create csv file
            for line in result:
                myfile.write(str(line))

            myfile.write("\n")

    @staticmethod
    def clear_file():
        open('/python-cources/HT_7/results.txt', 'w').close()

    @staticmethod
    def operations_count():
        with open('/python-cources/HT_7/results.txt') as f:
            count = len(f.readlines())

        return Calculator.write_to_file("Operations count - " + str(count))



Calculator.clear_file()
ins1 = Calculator()
print("Last result value - " + str(ins1.last_result))
res1 = ins1.add(5, 7)
res2 = ins1.substract(500, 70)
res3 = ins1.multiply(8, 9)
res4 = ins1.divide(67, 6)
Calculator.operations_count()


'''Написати програми з використанням 2х статік методів та 2х проперті'''
