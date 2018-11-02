from pymysql import connect

class MysqlHelp:
    def __init__(self, database, host='localhost',
                 user='root', password='123456',
                 charset='utf8', port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    # 连接数据库方法
    def open(self):
        # 　创建数据库连接对象conn
        self.conn = connect(host=self.host, user=self.user, password=self.password,
                            database=self.database, charset=self.charset,
                            port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

    # 关闭数据库方法
    def close(self):
        self.cur.close()
        self.conn.close()