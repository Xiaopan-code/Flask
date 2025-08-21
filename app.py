from flask import Flask, session, g
import config
from exts import db, mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)

app.register_blueprint(auth_bp)


# before_request/ before_first_request/ after_request 钩子函数
# hock
@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.get(user_id)
        # 设置一个全局变量 global
        setattr(g, 'user', user)
    else:
        setattr(g, 'user', None)


# 上下文处理器
@app.context_processor
def my_context_processor():
    # 之后在所以模板中都可以使用user user的值为当前的user对象
    return {'user': g.user}


if __name__ == '__main__':
    app.run()
