from bs4 import BeautifulSoup
import requests
import os
import csv
import xlsxwriter
import json
from time import sleep


try:
    directory = ("/python-cources/HT_8/reports/2")       # set path to reports directory
    if not os.path.exists(directory):
        os.makedirs(directory)                           # create directory if it doesn't exist
except Exception as e:
    print(e)


def collect_domains():
    initial_url = "https://www.expireddomains.net"
    has_next = True                                     # value by deafult for loop start
    next_page_url = '/deleted-biz-domains'
    while has_next:
        sleep(1)                                        # delay after each iteration. prevent blocking
        result = []
        url = initial_url + next_page_url               # create next page url
        page = requests.get(url)                        # get data from url
        soup = BeautifulSoup(page.content, 'html.parser')   # transfer data to bs
        links = soup.select('a.namelinks')              # find all links with domain names
        for link in links:
            result.append(link.text)                    # get text of each link (domain)

        write_to_csv(result)                            # write to 4 files
        write_to_xls(result)
        write_to_txt(result)
        write_to_json(result)
        try:
            next_page_url = soup.select('a.next')[0].get('href')        # find next page url
        except:
            has_next = False                                            # end loop if hasn't next page url


def write_to_csv(result):
    csv_file = open('reports/2/domains.csv', 'a')                       # add ability to write to the file end
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)            # initiate writer

    for i in result:
        csv_writer.writerow([i])                                        # write each domain to a file


def write_to_xls(result):
    workbook = xlsxwriter.Workbook('reports/2/domains.xls')
    worksheet = workbook.add_worksheet()                                # initiate worksheet

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, i)                                    # write each domain to a file
        row += 1                                                        # increase row number


def write_to_txt(result):
    with open('reports/2/domains.txt', 'a') as fp:                      # add ability to write to the file end
        fp.write(str(result))                                           # write object to a file
        fp.write('\n')                                                  # write next value from the new line


def write_to_json(result):
    with open('reports/2/domains.json', 'a') as fp:                     # add ability to write to the file end
        json.dump(result, fp)                                           # write object to a file
        fp.write('\n')                                                  # write next value from the new line


collect_domains()