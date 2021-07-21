from django.shortcuts import render
from models import *

# Create your views here.
def home():
    viewer()
    message = db_manager.last_row("messages")[0]
    return render_template("home.html", page_name="home", person=message[0] + message[1], txt=message[4])
