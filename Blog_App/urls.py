from django.urls import path
from Blog_App import views

urlpatterns = [
    path('',views.index,name='index'),
]