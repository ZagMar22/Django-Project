from django import forms
from django.forms import ModelForm
from .models import Topic


class AddTopic(ModelForm):

    class Meta:
        model = Topic
        fields = ('title', 'search_string', 'asset_description',)