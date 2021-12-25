
from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.main,name='main'),
    path('clear', views.clear,name='clear'),
    path('kill/', views.kill,name='kill'),
   
]
