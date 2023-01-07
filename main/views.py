from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDoList, Item, Topic, Ksiazka
from .forms import AddTopic, AddKsiazka

import matplotlib.pyplot as plt
import numpy as np

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})


def home(response):
    return render(response, "main/home.html", {})


def tabliczka(response):
    return render(response, "main/tabliczka.html", {})


def addtopic(request):
    form = AddKsiazka(request.POST or None)
    if form.is_valid():
        new_topic = form.save(commit=False)
        #kod do uzytkownika
        new_topic.save()

        return redirect('browse')
    context = {
        'form': form,
    }

    return render(request, "main/addtopic.html", context)

def browse(request):
    ksiazka_list = Ksiazka.objects.all()
    context = {
        'ksiazka_list': ksiazka_list,
    }  
    return render(request, "main/browse.html", context)


def update_ksiazka(request, ksiazka_id):
    ksiazka = Ksiazka.objects.get(pk=ksiazka_id)
    form = AddKsiazka(request.POST or None, instance=ksiazka)
    if form.is_valid():
        update_logiczne = form.save(commit=False)
        #kod do uzytkownika
        update_logiczne.save()
        return redirect("browse")
    context = {
        'ksiazka': ksiazka,
        'form': form,
    }  
    return render(request, "main/update_ksiazka.html", context)



def browsetopic(request, topic_id):
    ksiazka = get_object_or_404(Ksiazka, pk=topic_id)
    context = {
        'ksiazka': ksiazka,
    }  
    return render(request, "main/browsetopic.html", context)

def ajax(request):
    context = {
    }  
    return render(request, "main/ajax.html", context)



def wykresy(request):

    x = np.arange(0,4*np.pi,0.1)   # start,stop,step
    y = np.sin(x)
    plt.plot(x, y, color='green') 
    plt.title("Wykres Sinus")
    z = plt.show()

    context = {
        'z':z
    }  
    return render(request, "main/wykresy.html", context)



