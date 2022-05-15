import cgi
import sqlite3

form = cgi.FieldStorage()
user = {
    'fio': form.getfirst("text_fio", ""),
    'num': form.getfirst("text_num", ""),
    'country': form.getfirst("text_country", ""),
    'city': form.getfirst("text_city", ""),
    'index': form.getfirst("text_index", ""),
    'place': form.getfirst("text_place", "")
}

try:
    sqlite_connection = sqlite3.connect('turizm.db')
    cursor = sqlite_connection.cursor()
    info = cursor.execute(f"SELECT * FROM countries WHERE country = '{user['place']}'")
    if info.fetchone() is None:
        print("""Content-type: text/html\n
                      <!DOCTYPE HTML>
                            <html>
                            <head>
                                <meta charset="utf-8">
                                <title>Обработка данных форм</title>
                            </head>
                            <body>
                                <h1>Страны, в которую вы хотите отправиться, нет в списке</h1>
                                <a href = '/'>Назад</a>
                            </body>
                            </html>""")
        raise Exception
    else:
        sqlite_insert_query = f"INSERT INTO users (fio, phone, country, city, city_index) " \
                              f"values('{user['fio']}', '{user['num']}', '{user['country']}'," \
                              f" '{user['city']}', '{user['index']}')"
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()

        info = cursor.execute(f"SELECT * FROM countries WHERE country = '{user['place']}'").fetchone()
        info_user = cursor.execute(f"SELECT * FROM users WHERE phone = {user['num']}").fetchone()
        sqlite_insert_query = f"INSERT INTO tickets (user_id, user_fio, country_id, country) " \
                              f"values ({info_user[0]}, '{info_user[1]}', {info[0]}, " \
                              f"'{info[1]}')"
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("""Content-type: text/html\n
              <!DOCTYPE HTML>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Обработка данных форм</title>
                    </head>
                    <body>
                        <h1>Данные успешно отправлены {0} {1}</h1>
                        <a href = '/'>Назад</a>
                    </body>
                    </html>""".format(info, info_user))
        cursor.close()
except sqlite3.Error as error:
    print("""Content-type: text/html\n
              <!DOCTYPE HTML>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Обработка данных форм</title>
                    </head>
                    <body>
                        <h1>Данные не были отправлены из-за ошибки</h1>
                        <a href = '/'>Назад</a>
                    </body>
                    </html>""")
finally:
    if sqlite_connection:
        sqlite_connection.close()

