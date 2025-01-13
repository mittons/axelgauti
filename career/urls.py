from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_main, name='career_main'),
    path('old', views.career_main, name='career_main_old'),
    path('test/', views.test_view, name='career_main'),
]
