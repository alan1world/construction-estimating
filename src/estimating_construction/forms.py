from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import EmailField, TelField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')

class NewFullEnquiryForm(FlaskForm):
    fullname = StringField('Full name')
    company = StringField('Company')
    email = EmailField('Email')
    phone = TelField('Phone')
    sop = StringField('Project SOP code', validators=[DataRequired()])
    gateway = SelectField('Gateway', choices=[
        "0 - Mandate", 
        "1 - SOC Development",
        "2 - SOC-OBC Appraisal",
        "3 - OBC-FBC Detailed Design",
        "4 - Construction",
        ])
    description = StringField('Description')
    type = SelectField('Estimate type', choices=["Target", "Gateway", "CE Assessment"])
    partner = SelectField('Partner', choices=["Lot 1", "Lot 2", "N/A"])
    contract = SelectField('Contract', choices=["PSC", "ECC"])
    hub = SelectField('Hub', choices=[
        "North East", 
        "North West",
        'South East',
        'South West',
        'Midlands',
        'Eastern',
        ])
    submit = SubmitField('Submit')

class NewProjectForm(FlaskForm):
    sop = StringField('Project SOP code')
    description = StringField('Description')
    hub = StringField('Hub')
    submit = SubmitField('Submit')

class NewPersonForm(FlaskForm):
    fullname = StringField('Full name')
    company = StringField('Company')
    email = EmailField('Email')
    phone = TelField('Phone')
    submit = SubmitField('Submit')

class NewEnquiryForm(FlaskForm):
    gateway = StringField('Gateway')
    type = StringField('Estimate type')
    partner = StringField('Partner')
    contract = StringField('Contract')
    submit = SubmitField('Submit')

