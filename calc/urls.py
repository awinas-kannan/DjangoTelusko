from django.urls import path
# import calc.views
from . import views

urlpatterns = [
    path('', views.homepage,name ='home'),
    path('html', views.htmlhome,name ='htmlhome'),
    path('base', views.htmlhomewithbase,name ='htmlhomewithbase')
]
