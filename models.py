from exts import db
from datetime import datetime

# flask db init: 只需要执行一次
# flask db migrate: 将orm模型生成迁移成脚本
# flask db upgrade: 将迁移脚本映射到数据库中


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)


class QuestionModel(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    #  外键
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('UserModel', backref=db.backref('questions', lazy='dynamic'))


class AnswerModel(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # 外键
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # 关系
    question = db.relationship('QuestionModel', backref=db.backref('answers', order_by=create_time.desc()))
    author = db.relationship('UserModel', backref=db.backref('answers'))

