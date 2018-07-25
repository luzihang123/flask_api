# -*- coding:utf-8 -*-
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        '''
        自定义验证器
        :param value:
        :return:
        '''
        try:
            # 将用户传来的参数去枚举类中匹配，如果匹配失败，则抛出异常
            # 如果匹配成功则将int转换成枚举
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
