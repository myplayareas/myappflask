from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    name = StringField(label='Complete Name:')
    username = StringField(label='User Name:')
    email = StringField(label='Email Address:')
    password = PasswordField(label='Password:')
    confirma_password = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')