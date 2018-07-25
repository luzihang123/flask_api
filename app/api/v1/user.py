# -*- coding:utf-8 -*-
from app.libs.redprint import Redprint

# user = Blueprint('user', __name__)
api = Redprint('user')


@api.route('/v1/user/get')
def get_user():
    return 'i am clark'
