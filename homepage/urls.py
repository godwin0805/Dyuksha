from django.urls import path
from . import views

urlpatterns=[
    
    path("",views.homepage,name="homepage"),
    path("signin/",views.signin,name="login")
    ]