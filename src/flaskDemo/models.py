from flaskDemo.models import Product_T,Category_T,Size_T,Color_T,Order_T
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField,FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskDemo.models import User


sizes = Size_T.query.with_entities(Size_T.SizeID,Size_T.Size);
categories = Category_T.query.with_entities(Category_T.CategoryID, Category_T.CategoryType).distinct();
products = Product_T.query.with_entities(Product_T.ProductID).distinct();
orders = Order_T.query.with_entities(Order_T.OrderID).distinct();

for row in sizes:
    rowDict=row._asdict()
    sizes_choice = [(row['SizeID'],(row['Size'])) for row in sizes]

for row in categories :
    rowDict=row._asdict()
    categories_choice = [(row['CategoryID'],row['CategoryType']) for row in categories]
    
for row in products:
    rowDict=row._asdict()
    products_choice = [(row['ProductID'],row['ProductID']) for row in products]
    
for row in orders:
    rowDict=row._asdict()
    orders_choice = [(row['OrderID'],row['OrderID']) for row in orders]    


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    productName = TextAreaField('Product Description', validators=[DataRequired()])
    productColor = StringField('Product Color', validators=[DataRequired()])
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'png'])])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = FloatField('Product price', validators=[DataRequired()])
    size = SelectField("Size", choices=sizes_choice);
    category = SelectField("Category", choices=categories_choice);    
    submit = SubmitField('Add product')
    
class UpdateProductForm(FlaskForm):
    productName = TextAreaField('Product Description', validators=[DataRequired()])
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'png'])])
    price = FloatField('Product price', validators=[DataRequired()]) 
    submit = SubmitField('Update product')
    
class CartUpdateForm(FlaskForm):
    orderId = IntegerField('OrderID', validators=[DataRequired()])
    productId = SelectField("ProductID", choices= orders_choice)
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Update product')


class AddToCartForm(CartUpdateForm):
    submit = SubmitField('Add to Cart')    
