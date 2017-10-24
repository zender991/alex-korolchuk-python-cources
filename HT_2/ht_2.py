''' Task 1. Написати функцію season, приймаючу 1 аргумент — номер місяця (від 1 до 12),
яка буде повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).'''

#entered_value = int(input('Enter month number - '))   #input value

def season1(number):
    return print('First function : ' + str({1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer', 7:'summer', 8:'summer',
            9:'autumn', 10:'autumn', 11:'autumn', 12:'winter'}.get(number, 'Invalid number')))  #find month by key. key number equal month number

#season1(entered_value)

def season2(number):
    if number >= 3 and number <= 5:     #check ranges for seasons
        return 'spring'
    elif number >= 6 and number <= 8:
        return 'summer'
    elif number >= 9 and number <= 11:
        return 'autumn'
    elif number >= 1 and number <= 2 or number == 12:
        return 'winter'
    else:
        return 'Invalid number'   # if user entered more then 12 or less then 1 digit

#print('Second function : ' + str(season2(entered_value)))

def season3(number):
    seasones_list = ['winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
                     'autumn', 'autumn', 'autumn', 'winter', 'winter']  #initiate list of monthes

    if number >= 1 and number <= 12:
        return print('Third function : ' + str(seasones_list[number - 1]))  #find month by index in a list
    else:
        return  print('Third function : Invalid number')  # if user entered more then 12 or less then 1 digit

#season3(entered_value)
'''2. Написати функцію, яка буде приймати декілька значень, одне з яких значення за замовченням(повинна бути
перевірка на наявність),і у випадку якщо воно є додати його до іншого агрументу, якщо немає - придумайте
логіку що робити программі.'''


'''3. Створіть 3 різних функції(на ваш вибір), кожна з цих функцій повинна повертати якийсь результат. Також
створіть четверу ф-цію, яка в тілі викликає 3 попередніб обробляє повернутий ними результат та також повертає
результат. Таким чином ми будемо викликати 1 функцію, а вона в своєму тілі ще 3'''

#a = int(input('Enter first value - '))
#b = int(input('Enter second value - '))

def plus_digits(a, b):   #fubc makes addition with digits
    return a + b

def minus_digits(a, b):    #func makes subsctraction with digits
    return a - b

def multiply_digits(a, b):  #func makes multiplying with digits
    return a * b

def sum_of_all_funcs(a, b):  #find sum of addition, substraction and multiplying two numbers
    return print('Sum of all funcs values is : ' + str(plus_digits(a, b) + minus_digits(a, b) + multiply_digits(a, b)))

#sum_of_all_funcs(a, b)


'''
4. Створіть 2 змінні x та y з довільними значеннями;
Створіть просту умовну конструкцію(звісно вона повинна бути в тілі ф-ції), під час виконання якої буде
перевірятися рівність змінних x та y.
Удоскональте конструкцію та додайте відповідні умови, які б при нерівності змінних х та у відповідь повертали різницю чисел.
Повинні опрацювати такі умови:
x > y; відповідь - х більше ніж у на z
x < y; відповідь - у більше ніж х на z
x==y. відповідь - х дорівнює z
'''

#x = int(input('Enter x value - '))
#y = int(input('Enter y value - '))

def find_difference(x, y):
    if x > y:   #check if x bigger then y
        return print('x bigger then y to ' + str(x - y)) # x minus y if yes
    elif x < y: #check if y bigger then x
        return print('y bigger then x to ' + str(y - x))    # y minus x if yes
    else:
        return print('x and y are equal') #we haven't another situation else. only x equal y

#find_difference(x, y)


'''5.маємо рядок
створюєте ф-цію яка буде отримувати рядки на зразок мого, яка працює в 4 випадках:
якщо довжина рядка в дфапазоні 30-50 -> прінтує довжину, кількість букв та цифр
якщо довжина менше 30 -> прінтує суму всіх чисел та окремо рядок без цифр лише з буквами
якщо довжина бульше 50 - > ваша фантазія
звысно 4 все інше'''

test_string = "f98neRoi4Nr0c3n30irn03ien3c0rfekdNo400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"

def make_magic_with_string(entered_string):
    digits_count = 0    #iniate variables
    letters_count = 0
    only_letters_string = ''
    converted_string = ''
    if len(entered_string) >= 30 and len(entered_string) <= 50:
        for i in test_string:           #select each item in a string
            if i.isdigit():             #check type
                digits_count += 1       #if digit - increase counter
            elif i.isalpha():
                letters_count += 1      #if letter - increase counter
            else:
                pass                    #skip step if type is not str or int
        return print('All string length : ' + str(len(entered_string)) + ' Count of letters : ' + str(letters_count) +
                 ' Count of digits : ' + str(digits_count))

    if len(entered_string) < 30:
        for i in test_string:               #select each item in a string
            if i.isdigit():                 #check type
                digits_count += int(i)      #if digit - add digit to sum of all digits
            elif i.isalpha():               #check type
                only_letters_string += i    #if letter - add digit to a string
            else:
                pass                        #skip step if type is not str or int
        return print('Sum of all digits : ' + str(digits_count) + ' String without letters : ' + only_letters_string)

    if len(entered_string) > 50:
        for i in entered_string:            #select each item in a string
            if i.isdigit():                 #check type
                digits_count += int(i) * int(i)     #get square and add to sum
            elif i.isalpha():               #check type
                if i.islower():             #if letter in lowercase - make it in  uppercase
                    i = i.upper()
                else:
                    i = i.lower()            #if letter in uppercase - make it in  lowercase
                converted_string += i
            else:
                pass                        #skip step if type is not str or int
        return print("Sum of all digits in square : " + str(digits_count) + " Converted letters in string : " + converted_string)

    else:
        return print('Incorrect input data')


#make_magic_with_string(test_string)

'''6. придумайте 3 різних ф-ції(немає різниці які)'''

#I took tasks from HT1 and made them like functions

#6.1. check if entered value is present in a list

list = [5, 3, 'ololo', 1, 5.7, 'kokoko', 2, 12]
#value = int(input('Enter value - '))

def check_value_present(value, list):
    if value in list:       #check value present in a list
        return print('Value ' + str(value) + ' is present in a list') #print that value is present
    else:   #in another case - it can be only value is absent - print value is absent
        return print('Value ' + str(value) + ' is absent in a list')

#check_value_present(value, list)

#6.2. remove empty tuples from a list

test_list1 = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), ('d')]
new_list = []

def remove_empty_tuples(tuple):
    for i in tuple:  # select each tuple in a list
        if len(i) > 0:
            new_list.append(i)  # if tuple isn't empty - add to new list
    return print('List without empty tuples ' + str(new_list))

# remove_empty_tuples(test_list1)


# 6.3. get the maximum and minimum value in a dictionary.

input_dictionary = {1:10, 2:20, 3:10, 7:70, 8:10}

def find_max_and_min(test_dict):
    min_value = 10000000  # set large value for comparing
    max_value = 0
    for key,value in input_dictionary.items():  #select each value in a dictionary
        if value > max_value:  # if current value bigger then current max value, set current value as max value
            max_value = value
        elif min_value > value:
            min_value = value # if current value less then current min value, set current value as min value
    return print('Max value : ' + str(max_value) + ' - Min Value : ' + str(min_value))

#find_max_and_min(input_dictionary)