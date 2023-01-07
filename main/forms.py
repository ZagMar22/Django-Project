from django import forms
from django.forms import ModelForm
from .models import Topic, Ksiazka


class AddTopic(ModelForm):

    class Meta:
        model = Topic
        fields = ('title', 'search_string', 'asset_description',)


class AddKsiazka(ModelForm):

    class Meta:
        model = Ksiazka
        fields = ('imie', 'nazwisko', 'telefon',)