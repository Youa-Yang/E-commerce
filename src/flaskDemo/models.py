from datetime import datetime
from flaskDemo import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from flask_migrate import Migrate

db.Model.metadata.reflect(db.engine)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class Customer_T(db.Model):
    __table__ = db.Model.metadata.tables['customer_t']
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
class Order_T(db.Model):
    __table__ = db.Model.metadata.tables['order_t']

class Product_T(db.Model):
    __table__ = db.Model.metadata.tables['product_t']

class OrderLine_T(db.Model):
    __table__ = db.Model.metadata.tables['orderline_t']

class BillingAddress_T(db.Model):
    __table__ = db.Model.metadata.tables['billingaddress_t']

class ShippingAddress_T(db.Model):
    __table__ = db.Model.metadata.tables['shippingaddress_t']

class Category_T(db.Model):
    __table__ = db.Model.metadata.tables['category_t']

class Size_T(db.Model):
    __table__ = db.Model.metadata.tables['size_t']

class Color_T(db.Model):
    __table__ = db.Model.metadata.tables['color_t']
