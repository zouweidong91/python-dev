import os 
from sqlalchemy import create_engine as _engine
from sqlalchemy.engine import Engine

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_DATABASE = 'move_blog'
DB_USERNAME = 'root'
DB_PASSWORD = '123456'

# connect db
def create_engine(database) -> Engine:
    # 这个 Engine ，第一次返回时 create_engine() ，尚未实际尝试连接到数据库
    echo = os.environ.get('SQL_DEBUG', '').lower() in ('1', 'true')
    return _engine(
        "mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
            user = DB_USERNAME,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT,
            database = database
        ),
        echo = echo
    )
    # 这个 echo 标志是设置sqlachemy日志的快捷方式，\
    # 它是通过python的标准实现的。 logging 模块。启用它后，我们将看到生成的所有SQL
