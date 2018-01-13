insert_askstory_query = "INSERT INTO askstories (by, descendants, story_id, kids, score, text, time, title, type) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"