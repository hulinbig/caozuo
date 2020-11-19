#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'

from flask import Blueprint,request,render_template,redirect

user_bp = Blueprint('user', __name__)