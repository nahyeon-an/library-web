import pandas as pd
import pymysql

# library 데이터 확인
df = pd.read_csv("db/library-data.csv", encoding='CP949')
print(df.shape)
print(df.iloc[0])
print(df.info(verbose=True))
print(df.columns)
print("-"*100)

# db에 잘 들어갔나 확인
connection_info = {'host': 'localhost', 'user': 'ssacuser', 'password': 'ssac123!@#', 'db': 'libweb', 'charset': 'utf8'}

conn = pymysql.connect(**connection_info)
cursor = conn.cursor()

sql = "select * from library"
cursor.execute(sql)
result = cursor.fetchall()

conn.close()
print(pd.DataFrame(result))
print("-"*100)

# 시각장애인을 위한 도서목록 데이터 확인
df = pd.read_csv("db/books-for-blind.csv", encoding='CP949')
print(df.shape)
print(df.iloc[0])
print(df.info(verbose=True))
print(df.columns)