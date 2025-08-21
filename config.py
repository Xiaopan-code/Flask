SECRET_KEY = '200403308638'

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

# 邮箱配置
#
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '1141841975@qq.com'
MAIL_PASSWORD = 'zafxwdtxkpeuicjj'
MAIL_DEFAULT_SENDER = '1141841975@qq.com'
