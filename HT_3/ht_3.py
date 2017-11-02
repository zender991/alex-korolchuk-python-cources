from random import randint, uniform
import time

test_list = []
test_list_float = []

for i in range(5000):
    test_list.append(randint(0, 99))


for j in range(5000):
    test_list_float.append(uniform(0, 99.9))


def bubble_sort(list_for_bubble):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(list_for_bubble) - 1):
            if list_for_bubble[i] > list_for_bubble[i + 1]:
                temp = list_for_bubble[i]
                list_for_bubble[i] = list_for_bubble[i + 1]
                list_for_bubble[i + 1] = temp
                sorted = False

    return list_for_bubble



def insertion_sort(list):
    for i in range(len(list) - 1):

        curr_value = list[i]
        curr_index = i

        while curr_index > 0 and list[curr_index - 1] > curr_value:
            list[curr_index] = list[curr_index - 1]
            curr_index = curr_index - 1

    list[curr_index] = curr_value

    return list


def calculate_time(sort_func, sort_name):
    start_time = time.time()
    custom_sorted_list = sort_func(sort_name)
    time_diff = time.time() - start_time
    return time_diff, custom_sorted_list


def native_sort(initial_list):
    new_list = list(initial_list)       #make list copy, because func changes initial list
    new_list.sort()
    return new_list


def compare_lists(first_list, second_list):
    if first_list == second_list:
        return True
    else:
        return False



native_sorted_list = native_sort(test_list)   # get int sorted list with native sort function
native_sorted_list_float = native_sort(test_list_float)   # get float sorted list with native sort function


sorting_time_bubble_int, sorted_list_bubble_int = calculate_time(bubble_sort, test_list)   # get values for int bubble sorting
sorting_time_bubble_float, sorted_list_bubble_float = calculate_time(bubble_sort, test_list_float)   # get values for int bubble sorting

sorting_time_insertion_int, sorted_list_insertion_int = calculate_time(insertion_sort, test_list)   # get values for int bubble sorting



print('------ Sorting for int list ------')

#print('bubble sort: time = ' + str("{0:.4f}".format(sorting_time_bubble_int)) +            # display int bubble algorithm time, used .format for 4 digits after point,
#      ', The list is sorted correctly - ' + str(compare_lists(sorted_list_bubble_int, native_sorted_list)))      #return True if native and custom sorting results are equal

print('insertion sort: time = ' + str("{0:.4f}".format(sorting_time_insertion_int)) +            # display int bubble algorithm time, used .format for 4 digits after point,
      ', The list is sorted correctly - ' + str(compare_lists(sorted_list_insertion_int, native_sorted_list)))      #return True if native and custom sorting results are equal




print('------ Sorting for float list ------')
#print('bubble sort: time = ' + str("{0:.4f}".format(sorting_time_bubble_float)) +            # display float bubble algorithm time, used .format for 4 digits after point,
#      ', The list is sorted correctly - ' + str(compare_lists(sorted_list_bubble_float, native_sorted_list_float)))      #return True if native and custom sorting results are equal

