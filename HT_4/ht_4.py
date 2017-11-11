import re
import csv


file = open('test.log')

filetext = file.read()

#test_string = "2017-11-10 20:02:57,062 1176 ERROR pg openerp.addons.fetchmail.fetchmail: General failure when trying to fetch mail from pop server info@some_product.de."


result = re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} \d{4,5} (ERROR|WARNING|CRITICAL) \D{1,4} (.+)', filetext)

print(result)

with open('filename.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    t = ['line_id','marker', 'data_time', 'description']
    wr.writerow(t)
    line_id = 1
    for i in result:
        i = [line_id, i[1], i[0], i[2]]
        wr.writerow(i)
        line_id += 1