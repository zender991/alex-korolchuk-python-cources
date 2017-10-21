'''2. Write a script to print out a set containing all the colours from color_list_1
which are not present in color_list_2. '''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

#------------first implementation---------------

difference_set_1 = color_list_1 - color_list_2  #minus makes difference between sets
print(difference_set_1)

#------------second implementation---------------

difference_set_2 = color_list_1.difference(color_list_2) #method difference makes difference between sets
print(difference_set_2)

#------------third implementation---------------

color_list_3 = [] #initiate empty list

for color in color_list_1:  #select each color from the list 1
    if color not in color_list_2: #check selected color in the list 2
        color_list_3.append(color)  #add color that doesn't present in the list 2

difference_set_3 = set(color_list_3)
print(difference_set_3) #print new list with needed colors

