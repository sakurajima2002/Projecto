from django.urls import path
from Login import views

urlpatterns = [
    path('login/',views.logear,name='Login'),
    path('cerrar_session',views.cerrar_session,name='cerrar_session'),
]