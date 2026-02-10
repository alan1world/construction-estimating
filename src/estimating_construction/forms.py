from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms import EmailField, TelField, SelectField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


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


class DesignationsFormRadio(FlaskForm):
    designation = RadioField(choices=["Random", "Fixed", "None"])
    submit = SubmitField('Submit')


class DesignationsForm(FlaskForm):
    designation = MultiCheckboxField(choices=["Random", "Fixed", "None"])
    submit = SubmitField('Submit')


class EnquiriesModalSubform(FlaskForm):
    available_options = MultiCheckboxField('Preferences', choices=[])


class ProjectPriceFormRadio(FlaskForm):
    price = RadioField(choices=[
                                "Standard Project (£1m-£50m)",
                                "Major Project (£50m+)",
                                "Minor Project (below £1m)"],
                             )
    submit = SubmitField('Submit')


class SiteAccessRadio(FlaskForm):
    access = RadioField(choices=[
                                "Yes (Significant challenges in accessing materials and labour)",
                                "No (Easily accessible with no major logistical issues)",]
                             )
    submit = SubmitField('Submit')


class HazardousWasteRadio(FlaskForm):
    waste = RadioField(choices=[
                                "Yes",
                                "No",]
                             )
    submit = SubmitField('Submit')


class GroundConditionsRadio(FlaskForm):
    ground = RadioField(choices=[
                                "No issues",
                                "Minor issues",
                                "Severe issues",]
                             )
    submit = SubmitField('Submit')


class SpeciesForm(FlaskForm):
    species = MultiCheckboxField(choices=[
                                    "Common Species (e.g. native species with no special status)",
                                    "Migratory Species (e.g. species that move through the area seasonally)",
                                    "Protected Species (e.g. endangered or threatened species)",
                                    "Invasive Species (e.g. species that disrupt local ecosystems)",
                                    ])
    submit = SubmitField('Submit')
    
