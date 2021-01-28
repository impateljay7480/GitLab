from django.urls import path
from Blog_App import views

urlpatterns = [
    path('',views.index,name='index'),
    path('view/<int:id>/',views.blog_detail,name='view'),
    path('delete/<int:id>/',views.delete,name='delete'),


]