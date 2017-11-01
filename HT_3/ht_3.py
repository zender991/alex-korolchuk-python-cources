from random import randint
import time

#a = [34, 23, 56, 4]
a = []
for i in range(20):
    a.append(randint(0, 99))

#print(a)


def native_sort(list):
    list.sort()
    return list

def compare_lists(first_list, second_list):
    if first_list == second_list:
        return True
    else:
        return False


def bubble_sort(list):
    start_time = time.time()
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                sorted = False

            i = i + 1
    time_diff = time.time() - start_time

    return a



bubble_sort(a)
native_sort(a)

print('The list is sorted correctly - ' + str(compare_lists(bubble_sort(a), native_sort(a))))
