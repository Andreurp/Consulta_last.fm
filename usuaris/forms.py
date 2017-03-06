# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Login_Form (forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    helper = FormHelper()
    helper.form_class = 'col-lg-6 col-md-6'
    helper.field_class = 'col-lg-6 col-md-6'
    helper.add_input(Submit('login', 'Login', css_class='btn-primari'))

class RegistForm (forms.Form):
    username = forms.CharField(max_length = 100)
    email = forms.EmailField()
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())

    def clean_username(self):
        ##-------Comproba que no existeix aquest user-------##
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nom usuari ja existent.')
        return username