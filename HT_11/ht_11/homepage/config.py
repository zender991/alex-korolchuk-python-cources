# ----------- insert queries -----------

insert_askstories_query = "INSERT INTO askstories_askstories (author, descendants, story_id, kids, score, text, time, title, type, url) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_newstories_query = "INSERT INTO newstories_newstories (author, descendants, story_id, kids, score, text, time, title, type, url)" \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_jobstories_query = "INSERT INTO jobstories_jobstories (author, descendants, story_id, kids, score, text, time, title, type, url)" \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_showstories_query = "INSERT INTO showstories_showstories (author, descendants, story_id, kids, score, text, time, title, type, url)" \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# ----------- update queries -----------

update_askstories_query = "UPDATE askstories_askstories SET author = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

update_newstories_query = "UPDATE newstories_newstories SET author = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

update_jobstories_query = "UPDATE jobstories_jobstories SET author = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

update_showstories_query = "UPDATE showstories_showstories SET author = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

# ----------------------------------------

get_stories_id_query = "SELECT story_id FROM %s"
category_url_for_request = "https://hacker-news.firebaseio.com/v0/%s.json?print=pretty"
item_url_for_request = "https://hacker-news.firebaseio.com/v0/item/%i.json?print=pretty"
connect_to_db_credentials = "dbname='db_ht_11' user='postgres' host='localhost' password='newpassword'"
