from django.urls import path
from inicio import views
app_name='inicio'
urlpatterns = [
    path('',views.inicio, 'inicio:inicio'),
    path('prueba',views.prueba),
    path('segunda-vista', views.registro,name='registro'),
    path('crear_usuario/<str:nombre>/<str:apellido>/<str:mail>/<int:edad>/<str:genero>/',views.crear_usuario, name='crear_usuario'),
    
]