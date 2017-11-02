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



def insertion_sort(list_for_ins):

    for i in range(1, len(list_for_ins)):

        curr_value = list_for_ins[i]
        curr_index = i

        while curr_index > 0 and list_for_ins[curr_index - 1] > curr_value:
            list_for_ins[curr_index] = list_for_ins[curr_index - 1]
            curr_index = curr_index - 1

        list_for_ins[curr_index] = curr_value

    return list_for_ins


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



def print_result (test_list, sort_type ):


    native_sorted_list = native_sort(test_list)
    sorting_time, sorted_list = calculate_time(sort_type, test_list)

    return print(str(sort_type) + ' : time = ' + str("{0:.4f}".format(
        sorting_time)) +  # display int bubble algorithm time, used .format for 4 digits after point,
          ', The list is sorted correctly - ' + str(compare_lists(sorted_list,
                                                                  native_sorted_list)))  # return True if native and custom sorting results are equal



#print_result(test_list, bubble_sort)
#print_result(test_list, insertion_sort)
#print_result(test_list_float, bubble_sort)
#print_result(test_list_float, insertion_sort)


