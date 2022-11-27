from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDoList, Item, Topic
from .forms import AddTopic

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
    form = AddTopic(request.POST or None)
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
    topic_list = Topic.objects.all()
    context = {
        'topic_list': topic_list,
    }  
    return render(request, "main/browse.html", context)


def browsetopic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {
        'topic': topic,
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



