import pymysql

class SearchManager:
    def __init__(self, host, user, password, db):
        connection_info = {'host': host, 'user': user, 'password': password, 'db': db,
                           'charset': 'utf8'}
        self.conn = pymysql.connect(**connection_info)
        self.cursor = self.conn.cursor()

    def getLibaryInfo(self, name):
        sql = "select * from library where name="+name
        return "Library"