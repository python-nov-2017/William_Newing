from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): 
    context = {
        "time": datetime.now()
    }
    return render(request, "t_d/index.html", context)
    