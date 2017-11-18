import json
import requests
import argparse
import csv
import logging
import logging.config
import time
import datetime
import re
from config import category_list, default_category

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("exampleApp")

logger.info("Programm started")

arg_parser = argparse.ArgumentParser(description='Parser for categories')
arg_parser.add_argument("--cat","-c", type=str, choices=category_list, default=default_category, help="Category name")
arg_parser.add_argument("--score","-s", type=int, default=0, help="Score number")
arg_parser.add_argument("--date","-d", type=str, default="01/01/2000", help="Date in d/m/y format")
options = arg_parser.parse_args()
logger.info("Received category name - %s"%options.cat)

category = options.cat
score = options.score
date = time.mktime(datetime.datetime.strptime(options.date, "%d/%m/%Y").timetuple())

try:
    logger.info("Send request to get  categories IDs")
    category_url = ("https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"%category)
    response = requests.get(category_url, timeout=5)
    data = response.json()
    logger.info("Categories IDs received")
except Exception as e:
    logger.error(e)


json_list = []

for i in data[:20]:
    try:
        logger.info("Send request to get detailsed info about %i item" %i)
        url_for_items = ("https://hacker-news.firebaseio.com/v0/item/%i.json?print=pretty" % i)
        cur = requests.get(url_for_items, timeout=5)
        #cur = urllib.urlopen(url2, timeout=5)


        json_file = {
            "category": category,
            "item": cur.json()
            #"item": json.loads(cur.read())
        #     "item": {
        #         "fields": cur.json()
        #     },
        }

        json_list.append(json_file)
        #print(json_list)
        logger.info("Info about %i item stored" % i)
    except Exception as e:
        logger.error(e)




g = json.dumps(json_list)
u = json.loads(g)


filtered_list = []
for i in u:
    if i['item']['time'] >= date and i['item']['score'] >= score:
        try:
            a = re.search(r'(<[^>].*>)', i['item']['text'])
            i['item']['text'] = i['item']['text'].replace(a.group(0), " ")
            logger.info("Tags $s were removed")
        except:
            logger.info("Key text is absent in current item")

        filtered_list.append(i)

print(filtered_list)



with open('test.csv', 'w') as myfile:  # create csv file
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)      # initiate writer
    column_titles = ["category", "item"]  # set data for column titles
    wr.writerow(column_titles)      # write data for column titles
    for filtered_list in filtered_list:
        wr.writerow([filtered_list["category"],
                    filtered_list["item"]])
