from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CreateAgentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description')
    samples = StringField('samples')
