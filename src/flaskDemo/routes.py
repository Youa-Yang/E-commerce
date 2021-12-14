import os
import secrets
from PIL import Image
from sqlalchemy import func
from flask import render_template, url_for, flash, redirect, request
from flaskDemo import app, db, bcrypt
from flaskDemo.forms import RegistrationForm, LoginForm ,ProductForm,UpdateAccountForm,CreateOrderForm,UpdateProductForm
from flaskDemo.models import User, Post,Customer_T,Order_T,Product_T,OrderLine_T,BillingAddress_T,ShippingAddress_T,Category_T
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from sqlalchemy.exc import IntegrityError

@app.route("/")
@app.route("/home")
def home():
    results = Product_T.query.all()
    #results = Product_T.query.join(Category_T,Product_T.CategoryID == Category_T.CategoryType) \
    #           .add_columns(Product_T.ProductDescription,Product_T.ProductPrice, Category_T.CategoryType) ;
    return render_template('home.html', outString = results)
    


@app.route("/")
@app.route("/homeAdmin")
def homeAdmin():
    results = Product_T.query.all()
    #results = Product_T.query.join(Category_T,Product_T.CategoryID == Category_T.CategoryType) \
    #           .add_columns(Product_T.ProductDescription,Product_T.ProductPrice, Category_T.CategoryType) ;
    return render_template('homeAdmin.html', outString = results)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
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


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/product/<productId>")
@login_required
def product(productId):
    product = Product_T.query.get_or_404(productId);
    return render_template('product.html',title=str(product.ProductDescription)+"_"
                           +str(productId),product=product)
                           
                           
@app.route("/productAdmin/<productId>")
@login_required
def productAdmin(productId):
    product = Product_T.query.get_or_404(productId);
    return render_template('productAdmin.html',title=str(product.ProductDescription)+"_"
                           +str(productId),product=product)   

@app.route("/")
@app.route("/orders_admin")
def view_ordersAdmin():
    results01 = Customer_T.query.join(Order_T, Customer_T.CustomerID == Order_T.CustomerID).add_columns(Customer_T.CustomerID,Customer_T.CustomerName) \
        .join(OrderLine_T, OrderLine_T.OrderID == Order_T.OrderID).add_columns(OrderLine_T.OrderID,Order_T.OrderStatus)\
        .join(Product_T, Product_T.ProductID == OrderLine_T.ProductID).add_columns(Product_T.ProductDescription);
    return render_template('ordersAdmin.html', title='All orders', joined_m_n = results01)                     


@app.route("/productAdmin/<productId>/delete", methods=['POST'])
@login_required
def delete_product(productId):
    product = Product_T.query.get_or_404(productId);
    try:
        db.session.delete(product)
        db.session.commit()
        flash('The product has been removed from the inventory', 'success')
    except IntegrityError:
            flash('The product can not be deleted from inventory', 'danger')        
    return redirect(url_for('homeAdmin'))


@app.route("/product/new", methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
   # max_id = Product_T.query(func.max(Product_T.ProductID))
    if form.validate_on_submit():
        #max_id = Product_T.query(func.max(Product_T.ProductID))
        product = Product_T(ProductID = 7,ProductDescription=form.productName.data, ProductColor=form.productColor.data,
        ProductAvailableQuantity=form.quantity.data, SizeID = form.size.data,
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

    form = UpdateProductForm()
    if form.validate_on_submit():
        product.ProductDescription = form.productName.data
        product.ProductPrice = form.price.data
        db.session.commit()
        flash('Your product has been updated!', 'success')
        return redirect(url_for('productAdmin', productId=product.ProductID))
    elif request.method == 'GET':
        form.productName.data = product.ProductDescription
        form.price.data = product.ProductPrice
    return render_template('update_product.html', title='Update Product',
                           form=form, legend='Update Product')    


@app.route("/product/<productId>/order", methods=['GET', 'POST'])
@login_required
def order_product(productId):
    product = Product_T.query.get_or_404(productId);
  
    form = CreateOrderForm()
    order1 = Order_T()
    orderLine = OrderLine_T()
    if form.validate_on_submit():
        order1.OrderID = 107
        order1.OrderDate = datetime.utcnow()
        order1.CustomerID = 3330
        db.session.add(order1)
        db.session.commit()

        
        orderLine.OrderLineID = 1009
        orderLine.ProductQuantity = form.quantity.data
        orderLine.ProductID = productId
        orderLine.OrderID = order1.OrderID
        db.session.add(orderLine)
        db.session.commit()
        flash('The product has been added to your cart!', 'success')
        return redirect(url_for('home', productId=product.ProductID))
    elif request.method == 'GET':
        form.quantity.data = 0
        form.size.data = product.SizeID
        order1.OrderStatus = "Processing"
    return render_template('create_order.html', title='Buy Product',
                           form=form, legend='Buy Product')   

@app.route("/order_history/")
@login_required
def order_history():
    results3 = User.query.join(Customer_T, Customer_T.CustomerID == User.id) \
        .join(Order_T, Order_T.CustomerID == Customer_T.CustomerID).add_columns(Order_T.OrderID, Order_T.OrderStatus)\
        .join(OrderLine_T, OrderLine_T.OrderID == Order_T.OrderID).add_columns(OrderLine_T.ProductQuantity)\
        .join(Product_T, Product_T.ProductID == OrderLine_T.ProductID).add_columns(Product_T.ProductDescription);
    return render_template('order_history.html', title='Order History', joined_m_n = results3)

