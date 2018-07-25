# -*- coding:utf-8 -*-
# 枚举
from enum import Enum


class ClientTypeEnum(Enum):
    '''
    我们可以编写一个枚举类，来枚举所有的客户端类型。
    '''
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201


if __name__ == '__main__':
    type_client = ClientTypeEnum.USER_EMAIL
    print(type_client)

    value_client = ClientTypeEnum.USER_EMAIL.value
    print(value_client)

    print(ClientTypeEnum(200))

    print(type_client == ClientTypeEnum(200))

    print(ClientTypeEnum(100))

    print(type_client == ClientTypeEnum(100))
