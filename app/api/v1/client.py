# -*- coding:utf-8 -*-
from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('/register')
def create_client():
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    pass
