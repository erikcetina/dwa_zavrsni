from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import View
from main.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect




class HomePage(TemplateView):
    template_name = 'main/homepage.html'

class DjelatnikList(ListView):
    template_name = 'main/djelatnik_list.html'
    model = Djelatnik

class ProstorijaList(ListView):
    model = Prostorija

class OpremaList(ListView):
    model = Oprema

class RezervacijaList(ListView):
    model = Rezervacija




class LoginPageView(LoginView):
    template_name = 'authentication/login.html'
    next_page = "/homepage"