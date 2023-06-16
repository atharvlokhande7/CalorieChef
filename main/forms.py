from django.forms import ModelForm,ModelChoiceField
from django.forms import BaseInlineFormSet
from django.forms import BaseModelFormSet
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class CreateUserForm(UserCreationForm):
    class Meta:
        model = account
        fields = ['username','email','password1','password2','dob','height','weight','extype','gender']
        dob = forms.DateField(widget=AdminDateWidget)
        
class updateuser(ModelForm):
    class Meta:
        model = account
        fields = ['height','weight','extype','veg']
    
class updatehcon(ModelForm):
    hcon = forms.ModelMultipleChoiceField(
        label='Health Conditions',
        queryset=hcondition.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ) 
    
    class Meta:
        model = suser
        fields = ['hcon']
  
