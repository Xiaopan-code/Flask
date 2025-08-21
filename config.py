# 数据库配置文件
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'qa'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    PORT,
    DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
