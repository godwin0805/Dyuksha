from django.urls import path
from . import views

urlpatterns=[
    
    path("",views.homepage,name="homepage"),
    path("signup/",views.signup,name="login"),
    path("signup/signup",views.signup),
    path("signin",views.signin),
    path("signup/signin",views.signin),
    path("homepage/",views.homepage),
    path("signup/createevent",views.createevent),
    path("signup/event_create",views.event_create,name="event_create")
    ]