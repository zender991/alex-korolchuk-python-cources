'''8. Write a script to replace last value of tuples in a list.'''

initial_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
output_list = []
replace_value = 100
j = 0

for i in initial_list:              #select each tuple in a list
    a = list(i)                     #make it list, because you can change list
    a[len(i) - 1] = replace_value   #replce last value
    t = tuple(a)                    #convert changed list to tuple
    initial_list[j] = t             #replace old tuple to a new version
    j = j + 1                       #increase counter for list index

print(initial_list)
