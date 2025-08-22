from flask import Blueprint, request, render_template

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    return "欢迎来到问答平台首页"


# GET:渲染模板
# POST:把数据存储到数据库
@bp.route('/qa/public', methods=['GET', 'POST'])
def public_qa():
    if request.method == 'GET':
        return render_template("public_question.html")
