from flaskDemo.models import Product_T,Category_T
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField,FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskDemo.models import User


sizes = Product_T.query.with_entities(Product_T.ProductSize).distinct();
categories = Category_T.query.with_entities(Category_T.CategoryID, Category_T.CategoryType).distinct();


for row in sizes:
    rowDict=row._asdict()
    sizes_choice = [(row['ProductSize'],(row['ProductSize'])) for row in sizes]

for row in categories :
    rowDict=row._asdict()
    categories_choice = [(row['CategoryID'],row['CategoryType']) for row in categories]


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

class UpdateProductForm(FlaskForm):
    productName = TextAreaField('Product Description', validators=[DataRequired()])
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'png'])])
    price = FloatField('Product price', validators=[DataRequired()]) 
    submit = SubmitField('Update product')
    
    
class CreateOrderForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    size = SelectField("Size", choices=sizes_choice);
    productColor = StringField('Product Color', validators=[DataRequired()])
    submit = SubmitField('Add to cart') 
