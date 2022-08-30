from django.contrib import admin
from django.urls import path,include
from . import views

# from .views import about_me, resume, contact_me

urlpatterns = [
   path('',views.index,name='in'),
   # path('',views.tlb,name='tbb'),

]
