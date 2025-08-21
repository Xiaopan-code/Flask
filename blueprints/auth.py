from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message
from flask import request
import string
import random

# 都要以 /auth开头
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    pass


@bp.route("/register")
def register():
    # 验证用户提交的邮箱和验证码是否对应且正确
    return render_template("register.html")


@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是:{captcha}")
    mail.send(message)
    # 用数据库方式存储

    #用redis去存储
    return "success"


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["1141841975@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功!"
