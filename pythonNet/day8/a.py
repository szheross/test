from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient("localhost",27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class4

# 数据操作
print(dir(myset))

# 关闭连接
conn.close()