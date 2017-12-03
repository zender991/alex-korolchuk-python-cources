'''Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з
2-ма числами, а саме додавання, віднімання, множення, ділення.
Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
Результати записуються у файл.'''

class Calculator(object):

    def __init__(self):
        self.last_result = " "                  # set default value for last result

    def add(self, a, b):
        result_list = []                        # create empty list for result elements
        result_list.extend([a, " + ", b, " = ", a + b]) # add elements and result into a list
        return Calculator.write_to_file(result_list)    # write created list into a file

    def substract(self, a, b):                          # the same for othe operations
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
    def write_to_file(result):                  # use static method for write to a file
        with open('/python-cources/HT_7/results.txt', 'a') as myfile:  # write to a file end
            for line in result:
                myfile.write(str(line))                 # write each element from a list

            myfile.write("\n")      # add jump to a new line

    @staticmethod
    def clear_file():           # static method for clear file
        open('/python-cources/HT_7/results.txt', 'w').close()

    @staticmethod
    def operations_count():         # static method for count operations in a file
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
Calculator.operations_count()           # get operations count using static method


'''Написати програми з використанням 2х статік методів та 2х проперті
Програма обраховує загальну суму отриману вкладником, після закінчення депозиту. Відсотна ставка залежить від
терміну депозиту. Програма також виводить кількість вкладників'''

class Deposit(object):

    depositer_count = 0

    def __init__(self, duration = 12):
        self._duration = duration             # use private attribute
        Deposit.depositer_count += 1           # increase instance counter after each class init

    def calculate_sum(self, initial_sum):
        self.initial_sum = initial_sum
        result = self.initial_sum + self.percent        # calculate sum after deposit end
        return result

    @property
    def percent(self):                                      # use property percent. percent calculating depends on
        if self._duration >= 0 and self._duration < 6:      # duration.
            self._percent = 10
        if self._duration > 6 and self._duration <= 12:
            self._percent = 20

        return self._percent

    @property                                               # use property for get duration attribute
    def duration(self):
        return self._duration


    @staticmethod
    def get_depositer_count():                               # use static method for instnce count calculating
        return print("Instance count - " + str(Deposit.depositer_count))

    @staticmethod                               # use static method for calculating percent rate
    def find_percent(duration):                 # if user wants to know only percent rate, it doesn't need
        if duration >= 0 and duration < 6:      # to create instance
            percent = 10
        if duration > 6 and duration <= 12:
            percent = 20
        return print("Your percent will be - " + str(percent))


a = Deposit(3)
b = Deposit()
print(a.calculate_sum(100))
print(b.calculate_sum(100))     # totals are different bacause of different deposit duration
print(a.duration)               #check properties
print(a.percent)
Deposit.get_depositer_count()   # get depositers count
Deposit.find_percent(7)         # get percent rate if user wants to put money for 7 monthes