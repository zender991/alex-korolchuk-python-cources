'''5. Write a script to convert decimal to hexadecimal'''

decimal_numbers = [30, 4] #list of decimal numbers
hex_numbers = []

for number in decimal_numbers:  #select each decimal number
    hex_numbers.append(hex(number)[2:]) #convert to hex and add to a new list. [2:] to remove 0x

print(hex_numbers)