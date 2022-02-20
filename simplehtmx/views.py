from django.shortcuts import render
from .forms import GeeksForm
# Create your views here.


def index(request):
    form = GeeksForm()
    title = request.GET.getlist('title')
    description = request.GET.getlist('description')
    print(title)
    print(description)

    context = {
        "form" : form,
        "title" : title,
        "description": description,
    }

    return render(request, "index.html", context)

def getForm(request):
    form = GeeksForm()
    context = {
        "form" : form,
    }

    return render(request, "partials/getForm.html", context)