from django.urls import include, path
from models import views, admin
urlpatterns = [
    path('', views.index, name='index'),

]