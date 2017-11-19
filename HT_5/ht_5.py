'''
For run - type in command line:
python ht_5.py --cat category_name --score score_filter --date date_filter
--cat category_name - optional argument. use value by default. type - string. allowed values in config.py
--score score_filter - optional argument. use value by default. type - int.
--date date_filter  - optional argument. use value by default. type - string. format d/m/y
Example: python ht_5.py --cat askstories --score 1 --date 10/11/2010
'''

import json
import requests
import argparse
import csv
import logging.config
import time
import datetime
import re
import os
from config import category_list, default_category, default_date, default_score, reports_file_name, \
    reports_folder_name, categories_api_url, items_api_url



try:
    directory = ("/python-cources/HT_5/%s" % reports_folder_name)      # set path to reports directory
    if not os.path.exists(directory):
        os.makedirs(directory)                      # create directory if it doesn't exist
except Exception as e:
    print(e)


logging.config.fileConfig('logging.conf')
logger = logging.getLogger("exampleApp")

logger.info("-------------##############---------------")
logger.info("Programm started")

try:
    arg_parser = argparse.ArgumentParser(description='Parser for categories')
    arg_parser.add_argument("--cat","-c", type=str, choices=category_list, default=default_category, help="Category name")
    arg_parser.add_argument("--score","-s", type=int, default=default_score, help="Score number")
    arg_parser.add_argument("--date","-d", type=str, default=default_date, help="Date in d/m/y format")
    options = arg_parser.parse_args()
    logger.info("Received category name - %s"%options.cat)
except:
    logger.error("Incorrect input from a command line")

category = options.cat
score = options.score
date = time.mktime(datetime.datetime.strptime(options.date, "%d/%m/%Y").timetuple())

try:
    logger.info("Send request to get  categories IDs")
    category_url = (categories_api_url %category)
    response = requests.get(category_url, timeout=5)
    data = response.json()
    logger.info("Categories IDs received")
except Exception as e:
    logger.error(e)


json_list = []

logger.info("Send request to get detailed info about items in a category")
for i in data[:4]:
    try:
        logger.info("Send request to get detailsed info about %i item" %i)
        url_for_items = (items_api_url % i)
        cur = requests.get(url_for_items, timeout=5)

        json_file = {
            "category": category,
            "item": cur.json()
        }

        json_list.append(json_file)
        logger.info("Info about %i item stored" % i)
    except Exception as e:
        logger.error(e)

logger.info("Info about items is stored")


g = json.dumps(json_list)
u = json.loads(g)


filtered_list = []
for i in u:
    if i['item']['time'] >= date and i['item']['score'] >= score:
        try:
            a = re.search(r'(<[^>].*>)', i['item']['text'])
            if a is None:
                logger.info("There are no tags  in an item " + str(i['item']['id']))
            else:
                logger.info("Tags were removed in an item " + str(i['item']['id']))
        except:
            logger.info("Key text is absent in item " + str(i['item']['id']))

        filtered_list.append(i)

print(filtered_list)



try:
    with open('/python-cources/HT_5/%s/%s' % (reports_folder_name, reports_file_name), 'w') as myfile:  # create csv file
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)      # initiate writer
        column_titles = ["category", "item"]  # set data for column titles
        wr.writerow(column_titles)      # write data for column titles
        for filtered_list in filtered_list:
            wr.writerow([filtered_list["category"],
                        filtered_list["item"]])
except:
    logger.error("Can't create report file")

logger.info("Programm finished")
