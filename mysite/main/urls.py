from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('login', views.LoginPageView.as_view(), name='login'),
    path('homepage', views.HomePage.as_view(), name='homepage'),
    path('Djelatnik', views.DjelatnikList.as_view(), name='DjelatnikList'),
    path('Prostorija', views.ProstorijaList.as_view(), name='ProstorijaList'),
    path('Oprema', views.OpremaList.as_view(), name='OpremaList'),
    path('Rezervacija', views.RezervacijaList.as_view(), name='RezervacijaList'),
]