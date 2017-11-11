import re
import csv


file = open('test.log')
filetext = file.read()

result = re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} \d{4,5} (ERROR|WARNING|CRITICAL) \D{1,4} (.+)', filetext)


with open('filename.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    t = ['line_id','marker', 'data_time', 'description']
    wr.writerow(t)
    line_id = 1
    for i in result:
        i = [line_id, i[1], i[0], i[2]]
        wr.writerow(i)
        line_id += 1

counter = 0

unique_list = set(result)
unique_list1 = []
c_co = 0

for i in unique_list:
    for j in result:
        co = j.count(i[2])
        c_co += co
        #print(c_co)

    #unique_list1.append([list(i]])
    k = list(i)
    k.append(c_co)
    unique_list1.append(k)
    c_co = 0


with open('unique.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    t = ['count','marker', 'data_time', 'description']
    wr.writerow(t)
    for i in unique_list1:
        i = [i[3], i[1], i[0], i[2]]
        wr.writerow(i)


print(unique_list)
print(unique_list1)

