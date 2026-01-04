from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Portfolio-home'),  # <- ye change kaam karega
    path('download-cv/', views.download_cv, name='download_cv'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('content/', views.content, name='content'),
]

