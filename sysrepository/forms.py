from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, DataRequired

class RegisterForm(FlaskForm):
    name = StringField(label='Complete Name:', validators=[Length(min=2, max=50), DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=3), DataRequired()])
    confirma_password = PasswordField(label='Confirm Password:', validators=[Length(min=3), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=3, max=30), DataRequired()])
    submit = SubmitField(label='Sign in')

class RepositoryForm(FlaskForm):
    name = StringField(label='Repository Name:', validators=[Length(min=2, max=30), DataRequired()])
    link = StringField(label='Repository Link:', validators=[Length(min=2, max=500), DataRequired()])
    submit = SubmitField(label='New')