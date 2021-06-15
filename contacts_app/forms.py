from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, ValidationError
from contacts_app.models import User

class RegisterForm(FlaskForm):
    
    def validade_username(self, usarname_to_check):
        user = User.query.filter_by(username=usarname_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
        
    def validate_password(self, password):
        if len(password.data) < 6:
            raise ValidationError('Password must be 6 or more characters')

    username = StringField('User Name:', [validators.Length(min=4, max=30), validators.DataRequired(), validade_username])
    password1 = PasswordField('Password:', [validators.DataRequired(), validate_password, validators.DataRequired()])
    password2 = PasswordField('Conform Password:', [validators.EqualTo('password1', 'Password must match'), validators.DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
        
    username = StringField('User Name:', [validators.DataRequired()])
    password = PasswordField('Password:',[validators.DataRequired()])
    submit = SubmitField('Sing in')


class ContactForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=3), validators.DataRequired()])
    email = StringField('Email', [validators.Email()])
    phone = StringField('Phone', [validators.Length(max=20)])
    submit = SubmitField(label='Add Contact')
    edit = SubmitField(label='Edit')
    delete = SubmitField(label='Delete')
