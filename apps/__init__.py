#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'

from flask import Flask
import setting
from apps.user.view import user_bp
from exts import db
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')#app是一个核心对象
    app.config.from_object(setting.DevelopmentConfig)#加载配置,环境更改
    db.init_app(app) #将db对象于app进行了关联
    #注册蓝图
    app.register_blueprint(user_bp) #将蓝图对象绑定到app上
    print(app.url_map)
    return app