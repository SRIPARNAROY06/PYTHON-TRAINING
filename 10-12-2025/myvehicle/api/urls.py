from django.urls import path
from . import views

urlpatterns = [
    path('vehicles/', views.vehicles_list, name='vehicles_list'),  # GET all
    path('vehicles/<int:id>/', views.vehicle_detail, name='vehicle_detail'),  # GET single
    path('vehicles/create/', views.create_vehicle, name='create_vehicle'),  # POST
    path('vehicles/update/<int:id>/', views.update_vehicle, name='update_vehicle'),  # PUT
    path('vehicles/delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),  # DELETE
]

