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


make_magic_with_string(test_string)
