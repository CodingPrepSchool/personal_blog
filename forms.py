from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired


class Blog(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    post = TextAreaField('New Post', validators = [DataRequired()])
    submit = SubmitField("Create New Post")