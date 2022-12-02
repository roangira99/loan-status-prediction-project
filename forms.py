from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField, SelectField, FloatField

class AddRecord(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    gender = SelectField('select gender',
          choices=[('', ''), ('male', 'Male'),
          ('female', 'Female') ])
    married = SelectField('Are you married',
          choices=[('', ''), ('yes', 'Yes'),
          ('no', 'No') ])
    dependents = SelectField('select number of dependents',
          choices=[('', ''), ('0', '0'),
          ('1', '1'),
          ('2', '2'),
          ('3', '3+') ])
    education = SelectField('select education level',
          choices=[('', ''), ('graduate', 'Graduate'),
          ('notgraduate', 'Not Graduate') ])
    employed = SelectField('Are you Self Employed',
          choices=[('', ''), ('yes', 'Yes'),
          ('no', 'No') ])
    credit = SelectField('select Credit History',
          choices=[('', ''), ('0'),
          ('1.000000', '1.000000'),
          ('0.000000', '0.000000'),
          ('0.842199', '0.842199') ])
    area = SelectField('Select property area',
          choices=[('', ''), ('semiurban', 'Semiurban'),
          ('urban', 'Urban'),
          ('rural','Rural') ])
    applicantincome = FloatField('Applicant Income')
    coapplicantincome = FloatField('Copplicant Income')
    loanamount = FloatField('Loan Amount')
    loanamountterm = FloatField('Loan Amount Term')
    user_id = HiddenField()
    submit = SubmitField('Predict')
