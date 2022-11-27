from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("tabliczka", views.tabliczka, name="tabliczka"),
    path("addtopic", views.addtopic, name="addtopic"),
    path("browse", views.browse, name="browse"),
    path("browse/<topic_id>", views.browsetopic, name="browsetopic"),
    path("ajax", views.ajax, name="ajax"),
    path("wykresy", views.wykresy, name="wykresy"),

]