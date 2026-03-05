from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms import EmailField, TelField, SelectField, SelectMultipleField
from wtforms import HiddenField
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


class CostDriversStatusForm(FlaskForm):
    enqid = HiddenField()
    submit = SubmitField('Submit')


class CostDriversForm(FlaskForm):
    enqid = HiddenField()

    access = RadioField(
        choices=["Unconstrained", "Constrained"],
        label="What is the level of access to the site?",
    )
    access_detail = MultiCheckboxField(
        choices=[
            "Physically constrained access",
            "Time limited access (e.g. certain hours accessible)",
            "Third party access (e.g. access through land owned by others, access rights needed)",
        ],
    )

    designations = RadioField(
        choices=["No designation", "Designations:"],
        label="Are there any official designations for the site?",
    )
    designations_detail = MultiCheckboxField(
        choices=[
            "Area of outstanding natural beauty (AONB)",
            "National Park",
            "SSSIS, SACs, SPAs, Ramsar wetlands",
            "Marine Conservation Zones",
            "Conservation Zones",
            "TPO (Tree Protection Orders)",
        ],
    )

    site_compounds = MultiCheckboxField(
        choices=[
            "No compound (welfare only)",
            "Standard/main compound",
            "Satellite compound",
            "Highways",
        ],
        label="What types of site compounds do you have (if any)?",
    )

    site_access = RadioField(
        choices=[
            "No (Easily accessible with no major logistical issues)",
            "Yes (Significant challenges in accessing materials and labour)",
        ],
        label="Is the project in a remote location with difficult access to resources?",
    )

    price = RadioField(
        choices=[
            "Standard Project (£1m-£50m)",
            "Major Project (£50m+)",
            "Minor Project (below £1m)",
        ],
        label="How is the project classified?",
    )

    waste = RadioField(
        choices=["No", "Yes",],
        label="Is there any hazardous waste present on the site?",
    )

    ground = RadioField(
        choices=[
            "No issues",
            "Minor issues",
            "Severe issues",
        ],
        label="How would you describe the ground conditions on the site?",
    )

    existing_structures = RadioField(
        choices=["No requirement", "Requirements:"],
        label="What is required for the existing non-EA structures at the site?",
    )
    existing_structures_detail = MultiCheckboxField(
        choices=[
            "Removal (Complete demolition and disposal)",
            "Relocation or Diversion (Moving structures to a new location, service or road diversion)",
            "Partial Removal (Selective demolition and disposal)",
            "Protection of existing structures (existing structures in place)",
        ],
    )

    species = MultiCheckboxField(
        choices=[
            "Common Species (e.g. native species with no special status)",
            "Migratory Species (e.g. species that move through the area seasonally)",
            "Protected Species (e.g. endangered or threatened species)",
            "Invasive Species (e.g. species that disrupt local ecosystems)",
        ],
        label="What type of species are present/anticipated on the site?",
    )

    adverse_influence = RadioField(
        choices=["No", "Yes"],
        label="Is the project adversely influenced by any of the following?",
    )
    adverse_influence_detail = MultiCheckboxField(
        choices=[
            "Water",
            "Railway",
            "Highways",
            "Process Plants",
            "Buried pipelines",
            "Electricity routes",
        ],
    )

    milestone = RadioField(
        choices=[
            "Completion date set by programme logic (no constraints)",
            "Desirable completion used for completion date",
            "Seasonal deadline used for completion date",
            "Critical to complete by completion date",
        ],
        label="Is the project completion milestone constrained due to an external factor?",
    )

    missing_utilities = RadioField(
        choices=["None", "Missing:"],
        label="What utilities are not available to connect for the construction works?",
    )
    missing_utilities_detail = MultiCheckboxField(
        choices=[
            "Water",
            "Foul Water",
            "Power",
            "Data/Telecommunications",
        ],
    )

