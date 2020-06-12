from django.shortcuts import render
from mpttapp.models import File
from mpttapp.forms import FileAddForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "homepage.html", {'files': File.objects.all()})

def add_file(request):
    form = None
    if request.method == "POST":
        form = FileAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data["name"],
                parent=data["parent"]
            )
        return HttpResponseRedirect(reverse('homepage'))
    else:
        form = FileAddForm()
    return render(request, "add_file.html", {"form": form})
