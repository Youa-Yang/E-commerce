import os
import secrets
from PIL import Image
from sqlalchemy import func
from flask import render_template, url_for, flash, redirect, request
from flaskDemo import app, db, bcrypt
from flaskDemo.forms import RegistrationForm, LoginForm ,ProductForm
from flaskDemo.models import User, Post,Customer_T,Order_T,Product_T,OrderLine_T,BillingAddress_T,ShippingAddress_T,Category_T
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=products)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (225, 225)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn    


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/product/<productId>")
@login_required
def product(productId):
    assign = Product_T.query.get_or_404(productId);
    return render_template('assign.html',title=str(assign.ProductDescriprion)+"_"
                           +str(productId),assign=assign, now=datetime.utcnow())

@app.route("/view/<productId>/delete", methods=['POST'])
@login_required
def delete_product(productId):
    empProject = Product_T.query.get_or_404(productId);
    db.session.delete(empProject)
    db.session.commit()
    flash('The employee has been removed from the project', 'success')
    return redirect(url_for('home'))


@app.route("/product/new", methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
   # max_id = Product_T.query(func.max(Product_T.ProductID))
    if form.validate_on_submit():
        #max_id = Product_T.query(func.max(Product_T.ProductID))
        product = Product_T(ProductID = 7,ProductDescription=form.productName.data, ProductColor=form.productColor.data,
        ProductAvailableQuantity=form.quantity.data, ProductSize = form.size.data,
        ProductPrice= form.price.data, CategoryID = form.category.data,ProductImageFileName = form.image.data);
        db.session.add(product)
        db.session.commit()
        flash('Your product has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('add_product.html', title='Add new product',
                           form=form, legend='New Product')

@app.route("/")
@app.route("/home")
def customers():
    results = Customer_T.query.all()
    return render_template('customers.html', outString = results)


@app.route("/product/<productId>/update", methods=['GET', 'POST'])
@login_required
def update_product(productId):
    product = Product_T.query.get_or_404(productId);

    form = ProductForm()
    if form.validate_on_submit():
        product.ProductDescription = form.productName.data
        product.ProductPrice = form.price.data
        db.session.commit()
        flash('Your product has been updated!', 'success')
        return redirect(url_for('product', productId=product.ProductID))
    elif request.method == 'GET':
        form.productName.data = product.ProductDescription
        form.price.data = product.ProductPrice
    return render_template('add_product.html', title='Update Product',
                           form=form, legend='Update Product')    
