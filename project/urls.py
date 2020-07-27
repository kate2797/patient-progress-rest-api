from django.urls import path
from . import views

urlpatterns = [
    path('api/patients', views.patients, name='patients'),
    path('api/patients/<int:nhs_number>',
         views.patients_detail, name="patients_detail"),
]
