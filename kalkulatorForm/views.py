import django
from django.shortcuts import render

from .forms import ZamowienieForm
# Create your views here.
def home(request):
    title = "My Title"

    #add a form
    form = ZamowienieForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }
    return render(request,"base.html", context)

def calculator(request):
    context = { }
    return render(request, "calculator.html", context)

def about(request):
    context = { }
    return render(request, "about.html", context)