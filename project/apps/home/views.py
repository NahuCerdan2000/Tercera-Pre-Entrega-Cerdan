from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def index (request) :
    return render(request, "home/index.html")

def añadir_personal(request) :
    if request.method == "POST" :
        form = forms.PersonalForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("home/index.html")
    else:   
        form = forms.PersonalForm()
        context = {"form": form}
        return render(request="home/añadir_personal.html",Context=context)

def añadir_pais(request) :
    if request.method == "POST" :
        form = forms.PaisForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("home/index.html")
    else:   
        form = forms.PaisForm()
        context = {"form": form}
        return render(request="home/añadir_pais.html", Context=context)

def añadir_sector(request) :
    if request.method == "POST" :
        form = forms.SectorForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("home/index.html")
    else:   
        form = forms.SectorForm()
        context = {"form": form}
        return render(request="home/añadir_sector.html", Context=context)

