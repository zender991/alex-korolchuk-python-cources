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

response = requests.get("https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"%category)
data = response.json()

print(data)

json_list = []

for i in data:
    cur = requests.get("https://hacker-news.firebaseio.com/v0/item/%i.json?print=pretty"%i)
    json_file = {
        "category": category,
        "item": cur.json()
    #     "item": {
    #         "fields": cur.json()
    #     },
    }

    json_list.append(json_file)
    print(json_list)



# with open("file.txt", "w") as output:
#     output.write(json_list)
