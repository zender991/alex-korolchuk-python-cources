import psycopg2


conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='newpassword'")
cursor = conn.cursor()

# Выполняем запрос.
cursor.execute("SELECT * FROM test_table")
row = cursor.fetchone()


# Закрываем подключение.
cursor.close()
conn.close()
