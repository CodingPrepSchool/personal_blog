from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextAreaField, SubmitField, validators, StringField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class Blog(FlaskForm):
    date = DateField("Date", validators = [DataRequired()], format='%Y-%m-%d')
    new_post= TextAreaField("New Post", validators = [DataRequired()])
    submit = SubmitField("Create New Post") 
    