import flask_login
from contacts_app import app, db
from contacts_app.models import User, Contact
from contacts_app.forms import LoginForm, RegisterForm, ContactForm
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/contacts', methods=['GET', 'POST'])
@login_required
def contacts_page():
    current_user = flask_login.current_user
    contact_list = Contact.query.filter_by(user_id=current_user.id).all()
    form = ContactForm()
    return render_template('contacts.html', contact_list=contact_list, form=form)


@app.route('/new_contact', methods=['GET', 'POST'])
@login_required
def new_contact_page():
    form = ContactForm()
    if form.validate_on_submit():
        current_user = flask_login.current_user
        contact = Contact(name=form.name.data, email=form.email.data,
                          phone=form.phone.data, user_id=current_user.id)
        db.session.add(contact)
        db.session.commit()
        flash(f'{contact.name} has been successfully added! ', 'success')
    if form.errors:
        for field, err_msg in form.errors.items():
            flash(
                f'There was an error with add a new contact {field} {err_msg}', category='warning')
    return render_template('new_contact.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(
            f'Account as create successfully! You are now logged in as {user.username}', 'success')
        return redirect(url_for('home_page'))
    if form.errors:
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user {err_msg}', category='warning')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password(form.password.data):
            login_user(attempted_user)
            flash(
                f'Success! You are logged in as: {attempted_user.username}', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Username and password are not match! Please try again', 'warning')
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out!", category='success')
    return redirect(url_for('home_page'))


@app.route('/edit_contact/<int:contact_id>', methods=['POST'])
@login_required
def edit_contact(contact_id):
    form = ContactForm()
    if form.validate_on_submit():
        current_user = flask_login.current_user
        contact = Contact.query.get(contact_id)
        if contact.user_id == current_user.id:
            contact.name = form.name.data
            contact.email = form.email.data
            contact.phone = form.phone.data
            db.session.commit()
    return redirect(url_for('contacts_page'))


@app.route('/delete_contact/<int:contact_id>', methods=['POST'])
@login_required
def delete_contact(contact_id):
    current_user = flask_login.current_user
    contact = Contact.query.get(contact_id)
    if contact.user_id == current_user.id:
        db.session.delete(contact)
        db.session.commit()
    return redirect(url_for('contacts_page'))
