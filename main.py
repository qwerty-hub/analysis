import sqlite3
connection = sqlite3.connect('proxy.db')
cursor = connection.cursor()
#добавить атрибуты
cursor.execute('''CREATE TABLE IF NOT EXIST ProxyList
                Adress TEXT, Port TEXT''')