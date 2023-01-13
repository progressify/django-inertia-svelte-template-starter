from django.urls import path
from sample_app import views


app_name = 'sample_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
]
