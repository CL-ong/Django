from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("dank", views.dank, name="dank"),
    path("<str:name>", views.greet, name="greet")
]

