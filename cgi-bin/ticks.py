import sqlite3

sqlite_connection = sqlite3.connect('turizm.db')
cursor = sqlite_connection.cursor()

sqlite_insert_query = """SELECT * FROM tickets"""
count = cursor.execute(sqlite_insert_query)
print("""Content-type: text/html\n
          <!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>Билеты</title>
                </head>
                <body>""")
print("<h3>")
for row in count:
    print('ID билета: ', row[0])
    print("<br>")
    print('user id: ', row[1])
    print("<br>")
    print('user fio: ', row[2])
    print("<br>")
    print('country id: ', row[3])
    print("<br>")
    print('country: ', row[4])
    print("<br>")
    print("<br>")
print("</h3>")
print("""<br> <a href = '/'>Назад</a>
                </body>
                </html>""")