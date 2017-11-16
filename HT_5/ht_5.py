import json
import requests
import argparse
import csv
import logging
import logging.config
import time
import datetime
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
    category_url = ("https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"%category)
    response = requests.get(category_url, timeout=5)
    data = response.json()
except Exception as e:
    logger.error(e)

# response = urllib.urlopen(url, timeout=5)
# data = json.loads(response.read())

#print(data)

json_list = []

for i in data[:4]:
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



g = json.dumps(json_list)
u = json.loads(g)


bigger_noticed_date = []
for i in u:
    if i['item']['time'] >= date and i['item']['score'] >= score:
        bigger_noticed_date.append(i)

print(bigger_noticed_date)

# x = json.loads(json_list)
# f = csv.writer(open("test.csv", "wb+"))
# f.writerow(["category", "item", "title", "url", "descendants"])
#
# for x in x:
#     f.writerow([x["category"],
#                 x["item"]["title"],
#                 x["item"]["url"],
#                 x["item"]["descendants"]])


# with open("file.txt", "w") as output:
#     output.write(json_list)
