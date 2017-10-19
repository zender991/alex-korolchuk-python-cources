'''11. Write a script to remove duplicates from Dictionary.'''

input_dictionary = {1:10, 2:20, 3:10, 'color':'red', 7:70, 8:10}

dictionary_without_duplicates = {} #create empty dictionary

for key,value in input_dictionary.items():  #select each value in a dictionary
    if value not in dictionary_without_duplicates.values(): # check if value exists in dictionary without duplicates
        dictionary_without_duplicates[key] = value # add value if it is unique

print(dictionary_without_duplicates)

