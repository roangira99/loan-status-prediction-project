from re import template
from xmlrpc.client import boolean
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Predict
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import pickle
import numpy as np




app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Define the blueprint of the app
auth = Blueprint('auth', __name__)

@auth.route('/index')
def index():
    return render_template("index.html", user=current_user)

@auth.route('/services')
def services():
    return render_template("services.html", user=current_user)

@auth.route('/about')
def about():
    return render_template("about.html", user=current_user)

@auth.route('/contact')
def contact():
    return render_template("contact.html", user=current_user)

@auth.route('/eligibility', methods=['GET', 'POST'])
@login_required
def eligibility():
    form = Predict()
    return render_template("eligibility.html", user=current_user)

    

@auth.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method ==  'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

        new_form = Predict(gender=gender, married=married, dependents=dependents, education=education, employed=employed, credit=credit, area=area, applicantincome=ApplicantIncome, coapplicantincome=CoapplicantIncome, loanamount=LoanAmount, loanamountterm=Loan_Amount_Term)
        db.session.add(new_form)
        db.session.commit()
        

        # gender
        if (gender == "Male"):
            male=1
        else:
            male=0
        
        # married
        if(married=="Yes"):
            married_yes = 1
        else:
            married_yes=0

        # dependents
        if(dependents=='1'):
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif(dependents == '2'):
            dependents_1 = 0
            dependents_2 = 1
            dependents_3 = 0
        elif(dependents=="3+"):
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 1
        else:
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 0  

        # education
        if (education=="Not Graduate"):
            not_graduate=1
        else:
            not_graduate=0

        # employed
        if (employed == "Yes"):
            employed_yes=1
        else:
            employed_yes=0

        # property area

        if(area=="Semiurban"):
            semiurban=1
            urban=0
        elif(area=="Urban"):
            semiurban=0
            urban=1
        else:
            semiurban=0
            urban=0


        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)

        prediction = model.predict([[credit, ApplicantIncomelog,LoanAmountlog, Loan_Amount_Termlog, totalincomelog, male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes,semiurban, urban ]])

        # print(prediction)

        if(prediction=="N"):
            prediction="You are not qualified for a loan"
        else:
            prediction="You are qualified for a loan"


        return render_template("predictionresult.html", prediction_text="{}".format(prediction))

    else:
        return render_template("predictionresult.html")

@auth.route('/loancalc', methods=['GET', 'POST'])
@login_required # Ensure no one can access the logout page unless they are already logged in
def loancalc():
    return render_template("loancalc.html", user=current_user)

@auth.route('/home')
def home():
    return render_template("home.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required # Ensure no one can access the logout page unless they are already logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user) # Add a new user to the database
            db.session.commit() # Update the database
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


