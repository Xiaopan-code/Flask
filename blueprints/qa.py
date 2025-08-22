from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm, AnswerForm
from models import QuestionModel, AnswerModel
from exts import db
from decorators import login_required

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


# GET:渲染模板
# POST:把数据存储到数据库
@bp.route('/qa/public', methods=['GET', 'POST'])
@login_required
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
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # todo: 跳转到问答的详情页面
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for('qa.public_question'))


@bp.route('/qa/detail/<qa_id>')
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html", question=question)


# @bp.route('/answer/public', methods=['POST'])
@bp.post('/answer/public')
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, question_id=question_id, author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('qa.qa_detail', qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for('qa.qa_detail', qa_id=request.get('question_id')))


@bp.route('/search')
def search():
    # /search?q=flask
    # /search/<q>
    # post, request.form
    q = request.args.get('q')
    # 把标题中包含q这个关键字的问答/问题提取出来
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template('index.html', questions=questions)