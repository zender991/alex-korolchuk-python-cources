from random import randint
import time

#a = [34, 23, 56, 4]
test_list = []
for i in range(40):
    test_list.append(randint(0, 99))


def native_sort(list):
    list.sort()
    return list


def compare_lists(first_list, second_list):
    if first_list == second_list:
        return True
    else:
        return False


def calculate_time(f):
    start_time = time.time()
    print(start_time)
    f
    time_diff = time.time() - start_time
    print(time_diff)
    return time_diff



def bubble_sort(list):
    start_time = time.time()
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                sorted = False

    time_diff = time.time() - start_time

    return list


def insertion_sort(list):
    for i in range(len(list) - 1):

        curr_value = list[i]
        curr_index = i

        while curr_index > 0 and list[curr_index - 1] > curr_value:
            list[curr_index] = list[curr_index - 1]
            curr_index = curr_index - 1

    list[curr_index] = curr_value

    return list


#print("{0:.4f}".format(bubble_sort(a)))
#bubble_sort(a)
#native_sort(a)



print("{0:.4f}".format(calculate_time(bubble_sort(test_list))))
print('The list is sorted correctly - ' + str(compare_lists(bubble_sort(test_list), native_sort(test_list))))
print('The list is sorted correctly - ' + str(compare_lists(insertion_sort(test_list), native_sort(test_list))))
