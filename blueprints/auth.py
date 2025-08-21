from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from exts import mail, db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel, UserModel
from .forms import RegisterForm, LoginForm
from  werkzeug.security import generate_password_hash, check_password_hash

# 都要以 /auth开头
bp = Blueprint("auth", __name__, url_prefix="/auth")


# GET:返回模板
# POST:提交数据进行登录操作
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            # 存入到数据库的秘密是加密后的 先用邮箱去找用户进行查询
            user = UserModel.query.filter_by(email=email).first()
            # 如果没有用户说明邮箱不在数据库
            # 再次给它返回页面
            if not user:
                print("邮箱再数据库不存在!")
                return redirect(url_for("auth.login"))
            # 第一个加密后 第二个原密码
            if check_password_hash(user.password, password):
                # cookie
                # 不适合存储太多数据
                # 一般用来存放登录授权的东西
                # flask中的session 是经过加密后存储再cookie中的
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误!")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))



# 现在视图函数只能是GET/POST请求 用其他请求会出现405错误
# GER: 从服务器上获取数据
# POST: 将客户端数据提交给服务器
@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证: flask-wtf   wtf->wtforms
        form = RegisterForm(request.form)
        form.validate()
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


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
