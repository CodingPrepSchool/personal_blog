from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class NewPost(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    post = TextAreaField("New Post", validators = [DataRequired()])
    submit = SubmitField("Create New Post")