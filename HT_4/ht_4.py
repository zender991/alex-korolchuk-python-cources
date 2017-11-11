import re
import csv
import os


file = open('openerp-server.log')       # open log file
filetext = file.read()                  # write file object to variable

result = re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} \d{4,5} (ERROR|WARNING|CRITICAL) \D{1,4} (.+)',
                    filetext)           # reg exp for needed data


directory = "/python-cources/HT_4/reports"      # set path to reports directory
if not os.path.exists(directory):
    os.makedirs(directory)                      # create directory if it doesn't exist


with open('/python-cources/HT_4/reports/results.csv', 'w') as myfile:       # create csv file

    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)          # initiate writer
    column_titles = ['line_id','marker', 'data_time', 'description']        # set data for column titles
    wr.writerow(column_titles)                  # write data for column titles
    line_id = 1         # set id for first row
    for i in result:    # select each value in results
        i = [line_id, i[1], i[0], i[2]]     # re-order values inside item
        wr.writerow(i)      # write data in appropriate format to a file
        line_id += 1        # increase counter for line_id


#curr_count = 0
unique_list_full = []
repeat_counter = 0
for i in result:        # select each value in a list
    for j in result:    # run through all values in a list
        curr_count = j.count(i[2])  # calculate count of i[2] (description) values
        repeat_counter += curr_count    # write count to variable

    converted_to_list = list(i)     # convert tuple to list
    converted_to_list.append(repeat_counter)    # add count to current i
    unique_list_full.append(converted_to_list)  # add full line to new list
    repeat_counter = 0      # make 0 to counter for next iteration


l = 1
for i in unique_list_full:

    for j in unique_list_full[l:]:
        if i[2] == j[2]:
            unique_list_full.remove(j)

    l += 1


with open('/python-cources/HT_4/reports/unique.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    t = ['count','marker', 'date_time', 'description']
    wr.writerow(t)
    for i in unique_list_full:
        i = [i[3], i[1], i[0], i[2]]
        wr.writerow(i)