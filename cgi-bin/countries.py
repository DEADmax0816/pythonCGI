import sqlite3

sqlite_connection = sqlite3.connect('turizm.db')
cursor = sqlite_connection.cursor()

sqlite_insert_query = """SELECT country FROM countries"""
count = cursor.execute(sqlite_insert_query)
print("""Content-type: text/html\n
          <!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>Страны</title>
                </head>
                <body>""")
print("<h1>")
for row in count:
    print(row[0])
    print("<br>")
print("</h1>")
print("""<br> <a href = '/'>Назад</a>
                </body>
                </html>""")