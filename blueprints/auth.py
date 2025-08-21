from flask import Blueprint

# 都要以 /auth开头
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    pass
