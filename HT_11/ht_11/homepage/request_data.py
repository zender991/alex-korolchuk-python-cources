import requests
import psycopg2
from homepage.config import *


class Stories(object):
    conn = psycopg2.connect(connect_to_db_credentials)  # Connect to an existing database
    cursor = conn.cursor()  # Open a cursor to perform database operations

    @staticmethod
    def get_story_ids(category):                                    # get stories ids in selected category
        category_url = (category_url_for_request % category)
        response = requests.get(category_url, timeout=5)            # send request to api. get all categories IDs
        data = response.json()
        return data

    @staticmethod
    def get_story_details(i):                                       # get all fields from particular story
        url_for_items = (item_url_for_request % i)
        current_item = requests.get(url_for_items, timeout=5)
        current_story = current_item.json()
        return current_story

    @staticmethod
    def get_id_from_db(category):                                   # get id list of existing stories in DB
        Stories.cursor.execute(get_stories_id_query % category + '_' + category)
        id_list_from_db = [item[0] for item in Stories.cursor.fetchall()]   # generate list from query result
        return id_list_from_db

    @staticmethod
    def write_to_var_from_response(story_id):                       # write data from json into variables
        try:                                                        # each story may has different fields
            author = story_id['by']                                 # that's why using try..except for each variable
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

    def get_stories(self, story_title, insert_query, update_query):           # get detailed info of each story using  story id

        id_list = Stories.get_story_ids(story_title)                          # get stories ids in selected category
        id_list_from_db = Stories.get_id_from_db(story_title)                 # get unique id list from DB

        for i in id_list[:3]:                                                 # limit 3 request for category
            current_story = Stories.get_story_details(i)                      # get story json

            item_var = Stories.write_to_var_from_response(current_story)      # write values from json to variables

            if str(current_story['id']) not in id_list_from_db:               # compare received stories with exisitng in DB
                Stories.cursor.execute(insert_query,
                               (item_var[0], item_var[1], item_var[2], item_var[3], item_var[4],        # insert new story in DB
                                item_var[5], item_var[6], item_var[7], item_var[8], item_var[9]))
            else:
                Stories.cursor.execute(update_query,
                               (item_var[0], item_var[1], item_var[2], item_var[3], item_var[4],        # update existing story in DB
                                item_var[5], item_var[6], item_var[7], item_var[8], item_var[9], str(current_story['id'])))

            Stories.conn.commit()                                                      # make the changes to the database persistent


def execute():
    instance = Stories()
    instance.get_stories('askstories', insert_askstories_query, update_askstories_query)
    instance.get_stories('newstories', insert_newstories_query, update_newstories_query)
    instance.get_stories('jobstories', insert_jobstories_query, update_jobstories_query)
    instance.get_stories('showstories', insert_showstories_query, update_showstories_query)

