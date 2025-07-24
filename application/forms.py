from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, SelectField, DateField, HiddenField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets.html5 import NumberInput, DateInput

class LoginForm(FlaskForm):
    hidden_field = HiddenField(label = "Login Form")
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CreatePatientForm(FlaskForm):
    hidden_field = HiddenField(label = "Create Patient Form")
    ssn = StringField("SSN ID", validators=[DataRequired(), Length(min=9, max=9)])
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    bed_type = SelectField("Type of bed", 
                choices=[("general", "General ward"), ("sharing", "Semi sharing"), ("single", "Single room")])
    address = StringField("Address", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    submit = SubmitField("Create Patient")

class PatientIdForm(FlaskForm):
    hidden_field = HiddenField()
    patient_id = IntegerField("Patient ID", validators=[DataRequired()])
    check = SubmitField("Check")

class UpdatePatientForm(FlaskForm):

    hidden_field = HiddenField()
    patient_id = IntegerField("Patient ID", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()], widget=NumberInput())
    admission_date = DateField("Admission date", validators=[DataRequired()], widget=DateInput())
    bed_type = SelectField("Type of bed", 
                choices=[("general", "General ward"), ("sharing", "Semi sharing"), ("single", "Single room")])
    address = StringField("Address", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    update = SubmitField("Update")