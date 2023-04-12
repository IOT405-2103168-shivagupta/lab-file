from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def snapchat(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

#def greet(request,name):
#    return render(request,'greet.html'),


def index(request):
    return HttpResponse("hello everyone")


def about(request):
    return HttpResponse(" everyone")

def s1(request):
    return HttpResponse("studen1")




def date(request):
    current_datetime = datetime.date.now()  
    html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_datetime
    return HttpResponse(html)