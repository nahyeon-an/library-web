import pandas as pd
import pymysql

connection_info = {'host': 'localhost', 'user': 'ssacuser', 'password': 'ssac123!@#', 'db': 'libweb', 'charset': 'utf8'}

conn = pymysql.connect(**connection_info)
cursor = conn.cursor()

df = pd.read_csv("books-for-blind.csv", encoding='CP949')
df = df.where(pd.notnull(df), None)

for i in range(len(df)):
    author = df.iloc[i,0] # 저자
    title = df.iloc[i,1] # 책 제목
    publisher = df.iloc[i,2] # 출판사
    isbn = None

    if author is None:
        continue

    sql = "insert into blindbook (`author`,`title`,`publisher`,`isbn`) values (%s,%s,%s,%s)"

    cursor.execute(sql,(author, title, publisher, isbn))

conn.commit()

conn.close()