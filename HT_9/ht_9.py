import requests
import time
import os
from config import id_data_file_path, api_category_url, api_items_url


class Stories(object):
    from config import category_list            # import here because object Stories needs attribute 'category_list'
    id_list = []                                # create empty list for static method

    @staticmethod
    def get_id_from_file():                          # read all unique id from file

        if not os.path.exists(id_data_file_path):    # create file when it doesn't exist
            os.mknod(id_data_file_path)

        txt_file = open('data.txt', 'r')
        for i in txt_file:
            Stories.id_list.append(i)               # write unique ids to a list
        txt_file.close()

        return Stories.id_list

    @staticmethod
    def write_id_to_file(i):                        # write unique ids to a file
        with open("data.txt", "a") as file:
            file.write(str(i) + '\n')
        file.close()

    @staticmethod
    def create_html_file(title, data):              # create html file with timestamp in a title
        with open('%sresult.html' % title, 'w') as fp:
            fp.write(str(data))                     # add generated html into created file

    def get_story_ids(self, category):
        category_url = (api_category_url %category)
        response = requests.get(category_url, timeout=5)  # send request to api. get all categories IDs
        data = response.json()
        return data

    def get_title_stories(self, id_list):
        all_items_list = []
        current_id_list = []

        unique_id_list = Stories.get_id_from_file()         # get unique ids from a file

        for i in id_list:
            if i not in unique_id_list:                     # compare ids after request with unique ids
                current_id_list.append(i)                   # add new unique id to list for further actions
                Stories.write_id_to_file(i)                 # write new unique id to a file

        for i in current_id_list[:10]:                      # select each item in category.[:10] - limit for requests
            try:
                url_for_items = (api_items_url % i)         # send request to api. get info about current item
                current_item = requests.get(url_for_items, timeout=5)
                current_item_json = {                                   # create json for current item
                    "item": current_item.json()
                }

                all_items_list.append(current_item_json)                # add created json to final list
            except:
                pass

        return all_items_list

    def create_data_for_html(self, data_list):              # create list with data for html file
        title_list = []
        for i in data_list:
            a = "<li class='list-group-item'>" + i['item']['title'] + "</li>"
            title_list.append(a)

        title_string = ''
        for i in title_list:
            title_string += str(i)                          # add all elements from list to a string for html

        return title_string


instance = Stories()                                        # create instance
result_list = []                                            # list for all string with category info
ts = time.time()                                            # timestamp for html file title
for i in Stories.category_list:                             # select each category
    stories_id = instance.get_story_ids(i)                  # get ids for items
    stories_titles = instance.get_title_stories(stories_id)         # get stiries titles
    stories_string = instance.create_data_for_html(stories_titles)  # generate data for html
    result_list.append(stories_string)                              # add to a result list for html


# create structure for html file
html_file = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hometask - 9</title>
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="js/bootstrap.min.js"></script>



    <style>
    body {
        background-color: #1D1D1D;
        padding: 30px;
        margin: 0px;
    }
    #snowflakeContainer {
        position: absolute;
        left: 0px;
        top: 0px;
    }
    .snowflake {
        padding-left: 15px;
        font-family: Cambria, Georgia, serif;
        font-size: 14px;
        line-height: 24px;
        position: fixed;
        color: #FFFFFF;
        user-select: none;
        z-index: 1000;
    }
    .snowflake:hover {
        cursor: default;
    }
    </style>

</head>
<body>
<div id="snowflakeContainer">
	<p class="snowflake">*</p>
</div>
<h1 style="text-align: center; color: gray;">GeekHub Python Hometask 9</h1>
<div class="panel-group" id="collapse-group" style="
    padding: 10px;">
 <div class="panel panel-default">
 <div class="panel-heading">
 <h4 class="panel-title">
 <a data-toggle="collapse" data-parent="#collapse-group" href="#el1">Ask Stories</a>
 </h4>
 </div>
 <div id="el1" class="panel-collapse collapse in">
 <div class="panel-body">''' + result_list[0] + '''</div>
 </div>
 </div>
 <div class="panel panel-default">
 <div class="panel-heading">
 <h4 class="panel-title">
 <a data-toggle="collapse" data-parent="#collapse-group" href="#el2">Show Stories</a>
 </h4>
 </div>
 <div id="el2" class="panel-collapse collapse">
 <div class="panel-body">''' + result_list[1] + '''</div>
 </div>
 </div>
 <div class="panel panel-default">
 <div class="panel-heading">
 <h4 class="panel-title">
 <a data-toggle="collapse" data-parent="#collapse-group" href="#el3">New Stories</a>
 </h4>
 </div>
 <div id="el3" class="panel-collapse collapse">
 <div class="panel-body">''' + result_list[2] + '''</div>
 </div>
 </div>

 <div class="panel panel-default">
 <div class="panel-heading">
 <h4 class="panel-title">
 <a data-toggle="collapse" data-parent="#collapse-group" href="#el4">Job Stories</a>
 </h4>
 </div>
 <div id="el4" class="panel-collapse collapse">
 <div class="panel-body">''' + result_list[3] + '''</div>
 </div>
 </div>


</div>
<script src="js/fallingsnow_v6.js"></script>
<script src="js/prefixfree.min.js"></script>
</body>
'''

Stories.create_html_file(ts, html_file)     # write generated html to a file