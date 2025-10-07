from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create_blog'),
    path('doctor/', views.doctor_blogs, name='doctor_blogs'),
    path('patient/', views.patient_blogs, name='patient_blogs'),
]
