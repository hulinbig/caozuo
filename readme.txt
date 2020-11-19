1.模板
网页 ---》 模板引擎处理 ---》 模板
          render_template

{{ 变量 }}

{% if 条件 %} {%endif%}
for,block,macro,with

{% extends '' %}
{% include '' %}
{% import '' %}
{$ set username = '' %}

过滤器:

自定义过滤器
1.通过方法添加
2.装饰器


2.蓝图

1.flask-script
使用里面的Manager进行命令得到管理和使用：
manager  = Manager(app=app)

manager.run()  --->> 启动

使用命令在终端：
python app.py runserver

python app.py runserver -h 0.0.0.0 -p 5544

自定义添加命令：
@manager.command
def init():
    print("test")

python app.py init

2.数据库
mtv:
model 模型 ---》数据库
template  模板
view  视图

安装数据库组件
pip install pymysql  建立连接
pip install flask-sqlalchemy  实现ORM映射
pip install flask-migrate  实现命令--发布命令工具，操作ORM


步骤：
1.配置数据库的连接路径
 SQLALCHEMY_DATABASE_URI = 'mysql + pymysql://root:123456@127.0.0.1:3306/df'

2.创建包exts
    __init__.py中添加：
    db = SQLAlchemy()  ---->>> 必现于aoo联系

    def create_app():
        .....
        db.init_app(app)
        return app


3.migrate:
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


4.创建模型
    models.py
    模型就是类
    class User(db.Models):     ----->> user表
         id = db.Column(db.Integer, primary_key=True, autoincrement=True) #主键自动递增
         username = db.Column(db.String(15), nullable=False) #不为空
         password = db.Column(db.String(15), nullable=False)
         phone = db.Column(db.String(11), unique=True) #手机号唯一
         creat_time = db.Column(db.DateTime, default=datetime.now())

5.使用命令：
    a.强调。。。
        在app.py中导入模型：from apps.user.models import User
    b.在终端使用命令：db
    python app.py db init    ----->> 产生一个文件夹  migrations 初始化文件
    python app.py db migrate ----->> 自动产生了一个版本文件
    项目
        |---apps
        |---exts
        |---migrations  python app.py db init
                |--- versions 版本文件夹
                    |---1ca48090396c_.py --->>>python app.py db migrate 迁移
                                               python app.py db upgrade  同步
                                               python app.py db downgrade 降级
    python app.py db upgrade ----->> 在数据库创建表












