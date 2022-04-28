from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, SelectField, BooleanField, DateField
from wtforms.validators import DataRequired

class Postsforms(FlaskForm):
    date = DateField("Posted On:", validators=[DataRequired()], format = '%d/%m/%Y')
    post_message = StringField("Post:", validators=[DataRequired()])
    submit = SubmitField("Submit Post")