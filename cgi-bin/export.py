from lxml import etree as ET
import sqlite3

sqlite_connection = sqlite3.connect('turizm.db')
cursor = sqlite_connection.cursor()

usrs = cursor.execute("""SELECT * FROM users""").fetchall()
cursor.close()
root = ET.Element('table')

for row in usrs:
    main = ET.SubElement(root, 'user')
    info = ET.SubElement(main, 'ID')
    info.text = str(row[0])

    info = ET.SubElement(main, 'FIO')
    info.text = str(row[1])

    info = ET.SubElement(main, 'PHONE')
    info.text = str(row[2])

    info = ET.SubElement(main, 'COUNTRY')
    info.text = str(row[3])

    info = ET.SubElement(main, 'CITY')
    info.text = str(row[4])

    info = ET.SubElement(main, 'INDEX')
    info.text = str(row[5])


tree = ET.ElementTree(root)
tree.write('output.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")

with open('output.xml', 'r', encoding='UTF-8') as f:
    xml_out = f.readlines()

print("""Content-type: text/html\n
              <!DOCTYPE HTML>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Экспорт таблицы</title>
                    </head>
                    <body>""")

print("\n".join(xml_out))

print("""<a href = '/'>Назад</a>
                    </body>
                    </html>""")
