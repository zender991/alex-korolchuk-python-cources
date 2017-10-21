'''6. Write a script to check whether a specified value is contained in a group of values.'''

tested_list = [1, 5, 8, 3]
tested_tuple = (1, 5, 8, 3)

entered_value = int(input('Enter value - '))  #enter value

if entered_value in tested_list:  #check if value present in a list
    print(str(entered_value) + ' -> ' + str(tested_list) + ' : ' + 'True')
else:
    print(str(entered_value) + ' -> ' + str(tested_list) + ' : ' + 'False')


if entered_value in tested_tuple:  #check if value present in a tuple
    print(str(entered_value) + ' -> ' + str(tested_tuple) + ' : ' + 'True')
else:
    print(str(entered_value) + ' -> ' + str(tested_tuple) + ' : ' + 'False')
