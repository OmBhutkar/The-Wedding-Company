from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('create/', views.vendor_create, name='vendor_create'),
    path('<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('<int:pk>/update/', views.vendor_update, name='vendor_update'),
    path('<int:vendor_pk>/assign/', views.vendor_assign_from_detail, name='vendor_assign_from_detail'),
    path('<int:vendor_pk>/assign/<int:booking_pk>/', views.vendor_assign_to_booking, name='vendor_assign_to_booking'),
    path('assign/<int:booking_pk>/', views.vendor_assign, name='vendor_assign'),
]

