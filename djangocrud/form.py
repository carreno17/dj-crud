from django import forms
from .models import  CreateTask, Categories
from django.contrib.auth.models import User 


class FormTask(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title','class':'max-w-lg block w-full border-none shadow-sm text-sm rounded-md  focus:outline focus:outline-offset-0 focus:outline-yellow-500'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'max-w-lg block w-full border-none shadow-sm text-sm rounded-md   focus:outline focus:outline-offset-0 focus:outline-yellow-500'}), required=True)
    important = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': "h-4 w-4 text-yellow-400 focus:ring-yellow-400 rounded"}),  required=False)


    class Meta:
        model = CreateTask
        fields = ('title', 'description', 'important' )


