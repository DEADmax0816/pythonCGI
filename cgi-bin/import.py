from lxml import etree
import sqlite3

with open('input.xml', encoding='UTF-8') as f:
    xml_inp = f.read()

root = etree.fromstring(xml_inp)

s = []

for el in root.getchildren():
    t = []
    for i in el.getchildren():
        text = i.text
        t.append(text)
    s.append(t)

sqlite_connection = sqlite3.connect('turizm.db')
cursor = sqlite_connection.cursor()

for el in s:
    try:
        cursor.execute(f"INSERT INTO users(fio, phone, country, city, city_index) "
                   f"VALUES ('{el[1]}', '{el[2]}', '{el[3]}', '{el[4]}', '{el[5]}')")
        sqlite_connection.commit()
    except sqlite3.Error as error:
        print("""Content-type: text/html\n
                      <!DOCTYPE HTML>
                            <html>
                            <head>
                                <meta charset="utf-8">
                                <title>Импорт таблицы</title>
                            </head>
                            <body>
                                <h1>Данные не были отправлены из-за ошибки</h1>
                                <a href = '/'>Назад</a>
                            </body>
                            </html>""")
    finally:
        cursor.close()
        sqlite_connection.close()

print("""Content-type: text/html\n
              <!DOCTYPE HTML>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Обработка данных форм</title>
                    </head>
                    <body>""")

print(s)

print("""<a href = '/'>Назад</a>
                    </body>
                    </html>""")