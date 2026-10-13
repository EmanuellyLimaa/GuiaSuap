from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('login_administrador/', views.login_administrador, name='login_administrador'),
    path('tutoriais/', views.tutoriais, name='tutoriais'),
    path('logout/', views.logout_usuarios, name='logout'),
]