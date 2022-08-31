import sqlite3

conn = sqlite3.connect('aulDB.db')
print(type(conn))  # Output: <class 'sqlite3.Connection'>

ddl_create = """
  CREATE TABLE person (
    age TEXT NOT NULL,
    name TEXT NOT NULL
  );
"""
cursor = conn.cursor()  # criando um obj cursor
cursor.execute(ddl_create)  # cria tabela a partir do comando armazenado
cursor.execute('''INSERT INTO person VALUES ('20','galeno');''')
data = cursor.execute('''SELECT * FROM person''')

print('Created Table!')
print('Cursor Description: ', cursor.description)
print('Rows: ', cursor.rowcount)
for row in data:
  print(row)

cursor.close()
conn.close()