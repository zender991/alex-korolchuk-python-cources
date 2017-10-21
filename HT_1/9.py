initial_list = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), ('d')]
output_list = []


for i in initial_list:    #select each tuple in a list
    if len(i) > 0:
        output_list.append(i)   #if tuple isn't empty - add to new list


print(output_list)