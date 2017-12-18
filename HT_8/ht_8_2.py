from bs4 import BeautifulSoup
import requests
import os
import csv
import xlsxwriter
import json
from time import sleep


try:
    directory = ("/python-cources/HT_8/reports/2")  # set path to reports directory
    if not os.path.exists(directory):
        os.makedirs(directory)  # create directory if it doesn't exist
except Exception as e:
    print(e)


def collect_domains():
    initial_url = "https://www.expireddomains.net"
    has_next = True
    next_page_url = '/deleted-biz-domains'
    while has_next:
        sleep(1)
        print(next_page_url)
        result = []
        url = initial_url + next_page_url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.select('a.namelinks')
        for link in links:
            result.append(link.text)

        write_to_csv(result)
        write_to_xls(result)
        write_to_txt(result)
        write_to_json(result)
        try:
            next_page_url = soup.select('a.next')[0].get('href')
        except:
            has_next = False


def write_to_csv(result):
    csv_file = open('reports/2/domains.csv', 'a')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for i in result:
        csv_writer.writerow([i])


def write_to_xls(result):
    workbook = xlsxwriter.Workbook('reports/2/domains.xls')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, i)
        row += 1


def write_to_txt(result):
    with open('reports/2/domains.txt', 'a') as fp:
        fp.write(str(result))


def write_to_json(result):
    with open('reports/2/domains.json', 'a') as fp:
        json.dump(result, fp)


collect_domains()