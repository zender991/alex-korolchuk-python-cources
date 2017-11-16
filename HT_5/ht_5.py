import json
import requests
import argparse
import logging
import logging.config
from config import category_list, default_category

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("exampleApp")



#logging.basicConfig(filename="sample.log", level=logging.INFO)
logger.info("Programm started")

arg_parser = argparse.ArgumentParser(description='Parser for categories')
arg_parser.add_argument("--cat","-c", type=str, choices=category_list, default=default_category, help="Category name")
options = arg_parser.parse_args()
logger.info("Received category name - %s"%options.cat)
print(options.cat)


#category = "newstories"
category = options.cat

category_url = ("https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"%category)
response = requests.get(category_url, timeout=5)
data = response.json()



#
# response = urllib.urlopen(url, timeout=5)
# data = json.loads(response.read())


print(data)

json_list = []

for i in data:
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
    print(json_list)



# with open("file.txt", "w") as output:
#     output.write(json_list)
