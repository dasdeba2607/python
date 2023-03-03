from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators
from wtforms.validators import InputRequired, Email

class ContactForm(Form):
   name = StringField("Name Of Student")
   ## [validators.DataRequired("Please enter your name.")]

   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")

   email = StringField("Email")
   ## ,  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")]
   ## I need to do pip install email_validator for email validator https://stackoverflow.com/questions/61356834/wtforms-install-email-validator-for-email-validation-support
   ## https://stackoverflow.com/questions/25324113/email-validation-from-wtform-using-flask

   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])
   submit = SubmitField("Send")
