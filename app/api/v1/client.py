# -*- coding:utf-8 -*-
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 获取客户端信息
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        # 处理不同客户端注册的方案
        # 替代switchcase-{Enum_name:handle_func}
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
    # request.args.to_dict()

    # 表单：网页； json：移动端
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    pass


def __register_user_by_email():
    pass
