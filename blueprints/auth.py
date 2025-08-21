from flask import Blueprint, render_template, jsonify
from exts import mail, db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel

# 都要以 /auth开头
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    pass


@bp.route("/register")
def register():
    # 验证用户提交的邮箱和验证码是否对应且正确
    return render_template("register.html")

# bp.route: 如果没有指定methods参数，就默认是GET请求
@bp.route("/captcha/email")
def get_email_captcha():
    # 发送邮箱获得验证码
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # I/O: Input/Output 耗费事件太长了 放队列速度更快
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是:{captcha}")
    mail.send(message)
    # 用数据库方式存储
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # 用redis去存储
    # RESTful API
    # {code:200/400/500, message:"", data:{}}
    return jsonify({"code": 200, "message": "", "data": None})


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["1141841975@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功!"
