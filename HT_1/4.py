'''4. Write a script to concatenate N strings.'''

a = 'a'   #add defaul value for loop
final_string = ''

list_of_strings = []
while a != '':   #check if entered string not  empty
    a = input('Enter string (empty string for exit) - ')
    list_of_strings.append(a)  #add enter string to list of all entered strings


for i in list_of_strings:
    final_string = final_string + i + ' '    #add each element of a list to a string

print('Concatenated strings - ' + final_string)
