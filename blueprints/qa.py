from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm
from models import Question
from exts import db

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    return "欢迎来到问答平台首页"


# GET:渲染模板
# POST:把数据存储到数据库
@bp.route('/qa/public', methods=['GET', 'POST'])
def public_question():
    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        # form.validate_on_submit()
        # 这是一个组合判断，等效于 request.method == 'POST' and form.validate()
        # 只有当请求是 POST 方法（通常用于提交表单）且表单验证通过时，才会返回 True
        # 这是处理表单提交的推荐方式，因为它能避免在 GET 请求时就执行验证逻辑

        # form.validate()
        # 仅对表单数据进行验证，不判断请求方法
        # 无论请求是 GET、POST 还是其他方法，只要调用就会执行验证逻辑
        # 通常用于需要在非 POST 请求中进行表单验证的特殊场景
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            question = Question(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # todo: 跳转到问答的详情页面
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for('qa.public_question'))
