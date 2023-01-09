from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.browse, name="browse"),
    path("tabliczka", views.tabliczka, name="tabliczka"),
    path("addtopic", views.addtopic, name="addtopic"),
    path("browse", views.browse, name="browse"),
    path("browse/<topic_id>", views.browsetopic, name="browsetopic"),
    path("update_ksiazka/<ksiazka_id>", views.update_ksiazka, name="update_ksiazka"),
    path("ajax", views.ajax, name="ajax"),
    path("ranking", views.ranking, name="ranking"),
    path("wykresy", views.wykresy, name="wykresy"),
    path("search", views.search, name="search"),
    path("delete/<ksiazka_id>", views.delete_ksiazka, name="delete_ksiazka"),

]