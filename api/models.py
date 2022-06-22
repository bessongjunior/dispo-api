# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Junior Bessong
"""

from datetime import datetime

import json

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    # __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64)) 
    image_file = db.Column(db.String(20), default = 'default.jpg')
    post = db.relationship("ImageGPSData", lazy='select', backref = db.backref("author", uselist=False, lazy="joined")) #lazy status defined with backref()
    jwt_auth_active = db.Column(db.Boolean())
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    

    # def __init__(self, id):
    #     self.id = id

    def __repr__(self):
        return f"User '{self.username}','{self.email}','{self.image_file}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_email(self, new_email):
        self.email = new_email

    def update_username(self, new_username):
        self.username = new_username

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def toDICT(self):

        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['username'] = self.username
        cls_dict['email'] = self.email

        return cls_dict

    def toJSON(self):

        return self.toDICT()

    '''users email reset token'''

    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(api.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'users_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(api.config['SECRET_KEY'])
    #     try:
    #         users_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(users_id)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Admin(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64))
    image_file = db.Column(db.String(20), default='default.jpg')
    jwt_auth_active = db.Column(db.Boolean())
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    



    def __repr__(self):
        return f"Admin ('{self.fullname}','{self.email}','{self.image_file}')"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_email(self, new_email):
        self.email = new_email

    def update_username(self, new_username):
        self.username = new_username

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def toDICT(self):

        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['username'] = self.username
        cls_dict['email'] = self.email

        return cls_dict

    def toJSON(self):

        return self.toDICT()



    '''Admin email reset token'''
    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"

       
class ImageGPSData(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    gpslocation = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(32), unique=True, nullable=False)
    mlresult = db.Column(db.String(32), unique=True, nullable=False)
    picture_file = db.Column(db.String(20), default='default.jpg')
    date_posted = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)    #db.Reference('Users'),


    def __repr__(self):
        return f"ImageData: ('{self.gpslocation}', '{self.city}','{self.ml_result}', '{self.date_posted}')"

    def save(self):
        db.session.add(self)
        db.session.commit()


class JWTTokenBlocklist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jwt_token = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"Expired Token: {self.jwt_token}"

    def save(self):
        db.session.add(self)
        db.session.commit()
        
          
