

from django.urls import path
from stuapp.views import *

urlpatterns = [
    path('',index,name='index'),
]