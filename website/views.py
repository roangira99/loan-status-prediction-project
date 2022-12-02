# Stores all of the main views/ URL endpoint for the actual functioning frontend aspect of the website
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Predict
from . import db
import json

# Define the blueprint of the app
views = Blueprint('views', __name__)

# Defining a view/root to a page where the function will run whenever we go here
@views.route('/', methods=['GET', 'POST'])
@login_required # Decorator ensuring you cannot get to the homepage unless you log in
def home():
    return render_template("home.html", user=current_user)
