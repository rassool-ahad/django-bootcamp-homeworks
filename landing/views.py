from django.shortcuts import render
from models import *

# Create your views here.
def home(request):

    Massages.objects.all()
    return render_template("home.html", page_name="home", person=message[0] + message[1], txt=message[4])
