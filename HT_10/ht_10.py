import requests
import psycopg2
import time
from config import *

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='newpassword'")
cursor = conn.cursor()


class Stories(object):

    @staticmethod
    def get_story_ids(category):
        category_url = ("https://hacker-news.firebaseio.com/v0/%s.json?print=pretty" % category)
        response = requests.get(category_url, timeout=5)  # send request to api. get all categories IDs
        data = response.json()
        return data

    @staticmethod
    def get_story_details(i):
        url_for_items = ("https://hacker-news.firebaseio.com/v0/item/%i.json?print=pretty" % i)
        current_item = requests.get(url_for_items, timeout=5)
        current_story = current_item.json()
        return current_story

    @staticmethod
    def get_id_from_db(category):
        cursor.execute("SELECT story_id FROM %s" % category)
        id_list_from_db = [item[0] for item in cursor.fetchall()]
        return id_list_from_db

    @staticmethod
    def write_to_var_from_response(story_id):
        try:
            author = story_id['by']
        except:
            author = '-'
        try:
            descendants = story_id['descendants']
        except:
            descendants = '-'
        try:
            id = story_id['id']
        except:
            id = '-'
        try:
            kids = story_id['kids']
        except:
            kids = '-'
        try:
            score = story_id['score']
        except:
            score = '-'
        try:
            text = story_id['text']
        except:
            text = '-'
        try:
            time = story_id['time']
        except:
            time = '-'
        try:
            title = story_id['title']
        except:
            title = '-'
        try:
            type = story_id['type']
        except:
            type = '-'
        try:
            url = story_id['url']
        except:
            url = '-'

        return [author, descendants, id, kids, score, text, time, title, type, url]

    def get_stories(self, story_title, insert_query, update_query):

        id_list = Stories.get_story_ids(story_title)
        id_list_from_db = Stories.get_id_from_db(story_title)

        for i in id_list[:3]:
            current_story = Stories.get_story_details(i)

            item_var = Stories.write_to_var_from_response(current_story)

            if str(current_story['id']) not in id_list_from_db:
                cursor.execute(insert_query,
                               (item_var[0], item_var[1], item_var[2], item_var[3], item_var[4],
                                item_var[5], item_var[6], item_var[7], item_var[8], item_var[9]))
            else:
                cursor.execute(update_query,
                               (item_var[0], item_var[1], item_var[2], item_var[3], item_var[4],
                                item_var[5], item_var[6], item_var[7], item_var[8], item_var[9], str(current_story['id'])))

            conn.commit()


    @staticmethod
    def create_html_file(title, data):              # create html file with timestamp in a title
        with open('%sresult.html' % title, 'w') as fp:
            fp.write(str(data))                     # add generated html into created file
        fp.close()


    def get_data_from_db_for_html(self, category):
        title_list = []

        cursor.execute("SELECT title FROM %s" % category)
        titles_list_from_db = [item[0] for item in cursor.fetchall()]

        for i in titles_list_from_db:
            item_with_css_classs = "<li class='list-group-item'>" + i + "</li>"
            title_list.append(item_with_css_classs)

        title_string = ''
        for i in title_list:
            title_string += str(i)                          # add all elements from list to a string for html

        return title_string




instance = Stories()
# instance.get_stories('askstories', insert_askstories_query, update_askstories_query)
# instance.get_stories('newstories', insert_newstories_query, update_newstories_query)
# instance.get_stories('jobstories', insert_jobstories_query, update_jobstories_query)
# instance.get_stories('showstories', insert_showstories_query, update_showstories_query)
ts = time.time()
newstories = instance.get_data_from_db_for_html('newstories')
askstories = instance.get_data_from_db_for_html('askstories')
jobstories = instance.get_data_from_db_for_html('jobstories')
showstories = instance.get_data_from_db_for_html('showstories')
result_list = []
result_list.extend([newstories, askstories, jobstories, showstories])

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

cursor.close()
conn.close()

