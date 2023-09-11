from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('city_details/', views.city_details, name='city_details'),
    path('air-quality-data/', views.air_quality_data_list, name='air_quality_data_list'),
    path('air-quality-data/<uuid:data_id>/', views.air_quality_data_detail, name='air_quality_data_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user_view, name='user_profile')
]
