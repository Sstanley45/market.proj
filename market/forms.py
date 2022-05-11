from xml.dom import VALIDATION_ERR
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired
from market.models import User

class RegisterForm(FlaskForm):

      def validate_username(self, username_to_check):
            user = User.query.filter_by(username=username_to_check).first()
            if user:
                  raise VALIDATION_ERR('the user name already exists')

      username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
      email_address = StringField(label= 'Email:', validators=[Email(), DataRequired()])
      budget = IntegerField(label= 'Budget:', validators=[DataRequired()])
      password1 = PasswordField(label = 'password:', validators=[Length(min=6), DataRequired()]) 
      password2 = PasswordField(label = 'confirm password', validators=[EqualTo('password1'), DataRequired()]) 
      submit = SubmitField(label = 'Create Account')
      