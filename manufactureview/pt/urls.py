from django.urls import path
from django.conf.urls import url
from .views import ptView

urlpatterns = [
   path('',ptView().as_view()),
]