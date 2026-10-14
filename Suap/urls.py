from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('login_administrador/', views.login_administrador, name='login_administrador'),
    path('tutoriais/', views.tutoriais, name='tutoriais'),
    path('logout/', views.logout_usuarios, name='logout'),
    path('administrador/tutoriais/', views.gerenciar_tutoriais, name='gerenciar_tutoriais'),
    path('administrador/tutoriais/novo/', views.criar_tutoriais, name='criar_tutoriais'),
    path('administrador/tutoriais/<int:pk>/editar/', views.editar_tutorial, name='editar_tutorial'),
    path('administrador/tutoriais/<int:pk>/excluir/', views.excluir_tutorial, name='excluir_tutorial'),
    ]