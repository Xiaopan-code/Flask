from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message

# 都要以 /auth开头
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    pass


@bp.route("/register")
def register():
    return render_template("register.html")

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["1141841975@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功!"
