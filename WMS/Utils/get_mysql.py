import pymysql


class DBUtil:
    # 连接WMS数据库
    @classmethod
    def get_conn(cls):
        return pymysql.connect(host='192.168.10.128', port=3306, database='wms', user='root', password='123456',
                               charset='utf8')

    # 建立连接游标cursor
    @classmethod
    def get_cursor(cls, conn):
        if conn:
            return conn.cursor()
        else:
            raise Exception("请检查连接对象是否开启!")

    # 每次测试用例结束时关闭关闭两个对象
    @classmethod
    def quit_all(cls, cursor, conn):
        if cursor:
            cursor.close()
        else:
            raise Exception("请检查游标对象是否开启!")
        if conn:
            conn.close()
        else:
            raise Exception("请检查连接对象是否开启!")
