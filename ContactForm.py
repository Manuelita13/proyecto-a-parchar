from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', render_kw={"placeholder": "Your Name"})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)], render_kw={"placeholder": "Write your Message here..."})
    submit = SubmitField('Send')