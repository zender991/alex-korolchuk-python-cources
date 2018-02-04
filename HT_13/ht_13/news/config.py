# ----------- insert queries -----------

insert_story_query = "INSERT INTO news_story (author, descendants, story_id, kids, score, text, time, title, type, url, category_id_id) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# ----------- update queries -----------

update_story_query = "UPDATE news_story SET author = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s, category_id_id = %s " \
                          "WHERE story_id = %s"

# ----------------------------------------

get_stories_id_query = "SELECT story_id FROM news_story"
category_url_for_request = "https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"
item_url_for_request = "https://hacker-news.firebaseio.com/v0/item/%i.json?print=pretty"
connect_to_db_credentials = "dbname='ht_13' user='postgres' host='localhost' password='newpassword'"
