# Used to store the database models
from . import db # From the website (__init__.py) package import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_wtf import FlaskForm


# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     # **** Associating different information with different users ****
#     # Setting up a relationship between the note object and the user object
#     # We will use a foreign key (column in the database) to reference a column of another database
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     #  We must pass a valid ID of an exisiting user to this column when we create a note object

class Predict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String, nullable=False)
    married = db.Column(db.String, nullable=False)
    dependents = db.Column(db.String, nullable=False)
    education = db.Column(db.String, nullable=False)
    employed = db.Column(db.String, nullable=False)
    credit = db.Column(db.Float, nullable=False)
    area = db.Column(db.String, nullable=False)
    applicantincome = db.Column(db.Float, nullable=False)
    coapplicantincome = db.Column(db.Float, nullable=False)
    loanamount = db.Column(db.Float, nullable=False)
    loanamountterm = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self, gender, married, dependents, education, employed, credit, area, applicantincome, coapplicantincome, loanamount, loanamountterm):
    #     self.gender = gender
    #     self.married = married
    #     self.dependents = dependents
    #     self.education = education
    #     self.employed = employed
    #     self.credit = credit
    #     self.area = area
    #     self.applicantincome = applicantincome
    #     self.coapplicantincome = coapplicantincome
    #     self.loanamount = loanamount
    #     self.loanamountterm = loanamountterm

    



class User(db.Model, UserMixin):
    # Defining the schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # notes = db.relationship('Note') # Add to the user's note relationship the note ID. The Note table above is referenced
    predictions = db.relationship('Predict')
 
# You can store any other information by creating another class, define all the fields you would want to store for the 
# class (Look them up on flask sqlalchemy) and then add the foreign key to the user
