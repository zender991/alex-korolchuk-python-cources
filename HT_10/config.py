# ----------- insert queries -----------

insert_askstories_query = "INSERT INTO askstories (by, descendants, story_id, kids, score, text, time, title, type, url) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_newstories_query = "INSERT INTO newstories (by, descendants, story_id, kids, score, text, time, title, type, url)" \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_jobstories_query = "INSERT INTO jobstories (by, descendants, story_id, kids, score, text, time, title, type, url)" \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_showstories_query = "INSERT INTO showstories (by, descendants, story_id, kids, score, text, time, title, type, url)" \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# ----------- update queries -----------

update_askstories_query = "UPDATE askstories SET by = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

update_newstories_query = "UPDATE newstories SET by = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

update_jobstories_query = "UPDATE jobstories SET by = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"

update_showstories_query = "UPDATE showstories SET by = %s, descendants = %s, story_id = %s, kids = %s, score = %s, " \
                          "text = %s, time = %s, title = %s, type = %s, url = %s " \
                          "WHERE story_id = %s"
