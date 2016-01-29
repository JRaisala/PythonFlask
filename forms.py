from flask.ext.wtfimport Form
from wtformsimport StringField, PasswordField, SubmitField
from wtforms.validatorsimport Required

class FormName(Form):
    username = StringField('Enter your email',validators=[Required()],[Email()])
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Login');
    

class RegisterName(Form):
    email = StringField('Enter your email',validators=[Required()],[Email()])
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Register');
     