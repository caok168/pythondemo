#coding=utf-8
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager

app = Flask(__name__)
manager = Manager(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/Flask_test'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/Flask_test"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # user = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role:'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    address = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    fullName = db.Column(db.String(64))
    fullname = db.Column(db.String(64))
    # set foreign key
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:'.format(self.username)


if __name__ == '__main__':
    # db.create_all()
    manager.run()



