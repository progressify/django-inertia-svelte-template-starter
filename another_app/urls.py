from django.urls import path
from another_app import views


app_name = 'another_app'

urlpatterns = [
    path('contacts/', views.Contacts.as_view(), name='contacts'),
]
