import pymysql
conn = pymysql.connect(
    host= '127.0.0.1',
    port= 3306,
    user= 'root',
    passwd= 'root',
    db= 'mysql'
)

cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages WHERE id=1')
print(cur.fetchone())

cur.execute('DESCRIBE pages;')
columns = cur.fetchall()

# Exibir a descrição da tabela
for column in columns:
    print(column)

cur.execute('SELECT * FROM pages WHERE id=1')
results = cur.fetchall()

if results:
    for row in results:
        print(row)
else:
    print("Nenhum registro encontrado para id=1.")

cur.close()
conn.close()