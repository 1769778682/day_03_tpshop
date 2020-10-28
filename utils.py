import pymysql


class Mysql(object):
    __conn = None
    __cursor = None

    # 链接数据库
    @classmethod
    def __get_connect(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host='localhost',
                                         port=3306,
                                         user='root',
                                         password='root',
                                         database='books')
        return cls.__conn

    # 获取游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_connect().cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exe_sql(cls, sql):
        try:
            # 获取游标对象
            cursor = cls.__get_cursor()
            # 调用游标对象的execute方法，执行sql
            cursor.execute(sql)
            # 如果是查询
            if sql.split()[0].lower() == 'select':
                # 返回所有数据
                return cursor.fetchall()
            # 否则：
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回受影响的行数
                return cursor.rowcount
        except Exception as e:
            # 事务回滚
            cls.__conn.rollback()
            # 打印错误
            print(e)
        finally:
            cls.__close_cursor()
            cls.__close_connect()

    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_connect(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None
