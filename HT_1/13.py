'''13. Write a script to get the maximum and minimum value in a dictionary.'''

input_dictionary = {1:10, 2:20, 3:10, 7:70, 8:10}

min_value = 10000000  #set large value for comparing
max_value = 0

for key,value in input_dictionary.items():  #select each value in a dictionary
    if value > max_value:  # if current value bigger then current max value, set current value as max value
        max_value = value
    elif min_value > value:
        min_value = value # if current value less then current min value, set current value as min value

print('Max value : ' + str(max_value))
print('Min Value : ' + str(min_value))

