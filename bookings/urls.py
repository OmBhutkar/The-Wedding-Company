from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.booking_list, name='booking_list'),
    path('create/', views.booking_create, name='booking_create'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('<int:pk>/update/', views.booking_update, name='booking_update'),
    path('<int:booking_pk>/payment/create/', views.payment_create, name='payment_create'),
    path('<int:booking_pk>/timeline/create/', views.timeline_create, name='timeline_create'),
]


