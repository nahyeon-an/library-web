import pymysql


class SearchManager:
    def __init__(self, host, user, password, db):
        connection_info = {'host': host, 'user': user, 'password': password, 'db': db,
                           'charset': 'utf8'}
        self.conn = pymysql.connect(**connection_info)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def getBasicInfo(self, name=None):
        if name is None:
            sql = "select `name`, `sido_nm`, `gungu_nm` from `library`"
            self.cursor.execute(sql)
        else:
            sql = "select `name`, `sido_nm`, `gungu_nm` from `library` where `name` like %s"
            self.cursor.execute(sql, ('%' + name + '%',))
        result = self.cursor.fetchall()
        ret = []
        keys = ["name", "sido_nm", "gungu_nm"]
        for row in result:
            row_dict = {key: val for key, val in zip(keys, row)}
            ret.append(row_dict)
        return ret

    def getOperateTime(self, name):
        sql = """select `name`,`close_day`,`every_open`,`every_close`,`sat_open`,
                `sat_close`,`holiday_open`,`holiday_close` from `library` where `name`=%s"""
        self.cursor.execute(sql, (name,))
        result = self.cursor.fetchall()
        keys = ["name", "close_day", "every_open", "every_close", "sat_open",\
                "sat_close", "holiday_open", "holiday_close"]
        for row in result:
            row_dict = {key: val for key, val in zip(keys, row)}
            return row_dict

    def getDetailedInfo(self, name):
        sql = """select `name`,`close_day`,`every_open`,`every_close`,`sat_open`,
        `sat_close`,`holiday_open`,`holiday_close`,`seats`,`books`,`loanable_books`,
        `loanable_days`,`address`,`phone_number`
         from `library` where `name`=%s"""
        self.cursor.execute(sql, (name,))
        result = self.cursor.fetchall()
        keys = ["name", "close_day", "every_open", "every_close", \
                "sat_open", "sat_close", "holiday_open", "holiday_close", \
                "seats", "books", "loanable_books", "loanable_days", \
                "address", "phone_number"]
        ret = []
        for i, row in enumerate(result):
            row_dict = {key: val for key, val in zip(keys, row)}
            ret.append(row_dict)
        return ret

    def getAllData(self, *args):
        sql = "select "
        if len(args) == 0:
            print("missing columns")
            return
        for arg in args:
            sql += "%s, " % arg
        sql = sql[:-2]
        sql += " from `library`"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        ret = []
        for i, row in enumerate(result):
            row_dict = {key: val for key, val in zip(args, row)}
            ret.append(row_dict)
        return ret


if __name__ == '__main__':
    sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
    result = sm.getAllData("name", "sido_nm", "gungu_nm", "address")
    print(result)
    sm.close()
