from db_util import my_conn as con

def save_object(object):
    my_con = con.MysqlHelp()
    my_con.open()

    my_sql = 'insert into '
    my_sql += object.__dict__['cls']
    my_sql += ' values("888",46)'
    my_con.cur.execute(my_sql)
    my_con.commit()
    my_con.close()


def update_obiect(object):
    my_con = con.MysqlHelp()
    my_con.open()
    my_sql = 'update '
    my_sql += object.__dict__['cls']
    my_sql += ' set '
    for key in object.__dict__:
        if key !='cls' and object.__dict__[key]:
            my_sql += key
            my_sql += '="'
            my_sql += object.__dict__[key]
            my_sql += '"'
    my_sql += 'where id'
    my_sql += '="'
    my_sql += object.__dict__['id']
