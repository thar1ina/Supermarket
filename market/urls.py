from django.urls import path
from market import views

urlpatterns = [
    path('', views.prodyct, name='prodyct'),
    path('emp/', views.employee, name='emp')

]

