
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('ethos/', views.ethos, name='ethos'),
    path('key-skills/', views.key_skills, name='key_skills'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
]
