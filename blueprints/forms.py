import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db


# Form: 主要用于验证前端传过来的数据是否符合要求
class RegisterForm(wtforms.Form):
    # 指定验证器去看格式是否正确
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
    # 验证码不为4就错误
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误!")])
    # 用户名最少2位 最大20位
    username = wtforms.StringField(validators=[Length(min=2, max=20, message="用户名格式错误!")])
    # 密码最少6位 最大20位
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误!")])
    # 确定密码用上EqualTo 指定验证字段和上面的密码相等
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="两次密码不一致!")])

    # 自定义验证
    # 邮箱是否被注册
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册!")

    # 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        # 获取邮箱
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱/验证码错误!")
        # 用掉后就会删掉 数据库后面要去优化
        # todo: 可以把captcha_model删掉
        # else:
        #     db.session.delete(captcha_model)
        #     db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误!")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题长度错误!")])
    content = wtforms.StringField(validators=[Length(min=3, message="内容格式错误!")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="内容格式错误!")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要输入问题id!")])

