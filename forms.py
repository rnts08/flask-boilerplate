from flask_wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators

"""
    Example Registration Form
"""
class RegistrationForm(Form):
    name = TextField('Name', validators=[validators.DataRequired()])
    email = TextField('Email Address', [validators.Email(message=u'Invalid e-mail address')])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

