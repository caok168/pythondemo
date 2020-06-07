#!/usr/bin/python
# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

"""
flask_migrate作用：
1、通过命令的方式创建表
2、修改表的结构
"""


class Config(object):
    # SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/book"
    # "mysql+pymysql://root:root@127.0.0.1:3306/Flask_test"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/book"
    # 这个值可以设置,也可以不设置,如果不设置,那么会一直报警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 这里有个坑，下次再讲
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
manager = Manager(app)

# 第一个参数是flask实例，第二个参数SQLAlchemy实例
Migrate(app, db)

# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command("db", MigrateCommand)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    # title = db.Column(db.String(128))
    us = db.relationship("User", backref="role")


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    manager.run()


"""
实际操作顺序:
1.python database.py db init
2.python database.py db migrate -m"版本名(注释)"
3.python database.py db upgrade 然后观察表结构
4.根据需求修改模型
5.python database.py db migrate -m"新版本名(注释)"
6.python database.py db upgrade 然后观察表结构
7.若返回版本,则利用 python 文件 db history查看版本号
8.python database.py db downgrade(upgrade) 版本号
"""