'''7. Write a script to concatenate all elements in a list into a string and print it.'''

input_list = [30, 'test', 4, [3,5.1,8], 7]

string_with_elements = " "
for i in input_list: #select each value in the input list
    string_with_elements = string_with_elements + str(i) #add value to the string

print(string_with_elements)