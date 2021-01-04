import pandas as pd
import pymysql

connection_info = {'host': 'localhost', 'user': 'ssacuser', 'password': 'ssac123!@#', 'db': 'libweb', 'charset': 'utf8'}

conn = pymysql.connect(**connection_info)
cursor = conn.cursor()

df = pd.read_csv("library-data.csv", encoding='CP949')
df = df.where(pd.notnull(df), None)

for i in range(len(df)):
    name = df.iloc[i,0] # 도서관명
    sido_nm = df.iloc[i,1] # 시도명
    gungu_nm = df.iloc[i,2]  # 시군구명
    close_day = df.iloc[i,4]  # 휴관일
    every_open = df.iloc[i,5]  # 평일 오픈 시각
    every_close = df.iloc[i,6]  # 평일 종료 시각
    sat_open = df.iloc[i,7]  # 토요일 오픈 시각
    sat_close = df.iloc[i,8]  # 토요일 종료 시각
    holiday_open = df.iloc[i,9]  # 공휴일 오픈 시각
    holiday_close = df.iloc[i,10]  # 공휴일 종료 시각
    seats = df.iloc[i,11].item() # 열람 좌석수
    books = df.iloc[i,12].item()  # 도서 자료수
    loanable_books = df.iloc[i,15].item()  # 대출가능권수
    loanable_days = df.iloc[i,16].item()  # 대출가능일수
    address = df.iloc[i,17]  # 도로명 주소
    phone_number = df.iloc[i,19]  # 전화번호
    site = df.iloc[i,22]  # 홈페이지

    sql = """insert into library (`name`,`sido_nm`,`gungu_nm`,`close_day`,`every_open`,`every_close`,
    `sat_open`,`sat_close`,`holiday_open`,`holiday_close`,`seats`,`books`,`loanable_books`,`loanable_days`,
    `address`,`phone_number`,`site`) 
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    cursor.execute(sql,(name,sido_nm,gungu_nm,close_day,every_open,every_close,sat_open,sat_close,\
                        holiday_open,holiday_close,seats,books,loanable_books,loanable_days,\
                        address,phone_number,site))

conn.commit()

conn.close()