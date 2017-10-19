'''10. Write a script to concatenate following dictionaries to create a new one.'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

concatenated_dictionary = {}  #create empty dictionary
concatenated_dictionary.update(dic1) #use update method to add values from dic1 to cancatenated dictionary
concatenated_dictionary.update(dic2) # the same
concatenated_dictionary.update(dic3) # the same

print(concatenated_dictionary)