'''Написати функцію season, приймаючу 1 аргумент — номер місяця (від 1 до 12),
яка буде повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).'''


def season1(number):
    return {1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer', 7:'summer', 8:'summer',
            9:'autumn', 10:'autumn', 11:'autumn', 12:'winter'}.get(number)

# example - season1(7)

def season2(number):
    if number >= 3 and number <= 5:
        return 'spring'
    elif number >= 6 and number <= 8:
        return 'summer'
    elif number >= 9 and number <= 11:
        return 'autumn'
    else:
        return 'winter'

# example - season2(7)



entered_value = int(input('Enter month number - '))

print('First function : ' + str(season1(entered_value)))
print('Second function : ' + str(season2(entered_value)))