'''9. Write a script to remove an empty tuples from a list of tuples'''

initial_list = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), ('d')]

j = 0

for i in initial_list:              #select each tuple in a list
    if len(i) == 0:                 #chech if tiple is empty
        del initial_list[j]         #if empty, remove tuple from a list by index
    j = j + 1                       #increase conter for indexes

print(initial_list)
