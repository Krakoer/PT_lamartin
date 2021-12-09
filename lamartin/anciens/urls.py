from django.urls import path

from . import views

app_name="anciens"
urlpatterns = [
    path('', views.anciens, name='anciens'),
    path('<int:ancien_id>/', views.ancien, name='ancien'),
    path('<int:ancien_id>/edit', views.edit_ancien, name='edit'),
    path('create/', views.create, name="create"),
]