'''14. Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).'''

entered_number = int(input('Enter number - '))

output_dictionary = {}
numbers = []

while entered_number != 0:  #find all numbers between 1 and n
    numbers.append(entered_number)
    entered_number -= 1

for number in sorted(numbers):  #method sorted for order values inside a dictionary by ascending
    output_dictionary[number] = number * number #set key and value

print(output_dictionary)
