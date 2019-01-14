#-*- coding: utf-8 -*-
from django import forms
from web.models import Dreamreal

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Dreamreal.objects.filter(name = username)

      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()

class DreamrealForm(forms.Form):
   website = forms.CharField(max_length = 100)
   name = forms.CharField(max_length = 100)
   phonenumber = forms.CharField(max_length = 50)
   email = forms.CharField(max_length = 100)

class AddForm(forms.Form):
   a = forms.IntegerField()
   b = forms.IntegerField()
   b = forms.IntegerField()