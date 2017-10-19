'''1 .Write a script which accepts a sequence of comma-separated numbers
from user and generate a list and a tuple with those numbers.'''

input_data = input('Enter numbers divided by comma separator - ')

input_data = input_data.replace(',','')

generated_list = input_data.split()
generated_tuple = tuple(generated_list)

print('Output :')
print('List : ' + str(generated_list))
print('Tuple : ' + str(generated_tuple))