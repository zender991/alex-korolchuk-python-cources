'''3. Write a script to sum of the first n positive integers.'''

count_of_positive_numbers = input('Enter count of positive numbers - ') #get count

sum_of_all_positive_numbers = sum(range(int(count_of_positive_numbers) + 1)) #use range method for finding all disgits from 1 to n
                                                                             # + 1, because calculating from 0
print(sum_of_all_positive_numbers) #display results 