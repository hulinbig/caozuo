#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
from exts import db
from datetime import datetime
#ORM 类 ---》》 表
#类对象 ----》》表中的一条记录

class User(db.Model):
    #db.Colum(类型，约束，) 映射表中的字段
    '''
     类型：
     db.Integer  --->> int
     db.String(15) --->> varchar(15)
     db.DateTime --->> datetime
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #主键自动递增
    username = db.Column(db.String(15), nullable=False) #不为空
    password = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(11), unique=True) #手机号唯一
    creat_time = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return self.username

class Age(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键自动递增
    username = db.Column(db.String(15), nullable=False)  # 不为空
    password = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(11), unique=True)  # 手机号唯一
    creat_time = db.Column(db.DateTime, default=datetime.now())
