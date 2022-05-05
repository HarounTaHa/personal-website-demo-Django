from django.urls import path
from .views import index, contact, project_details, service_details

app_name = 'portfolio'

urlpatterns = [
    path('', index, name='index'),
    path('send-msg/', contact, name='contact'),
    path('service/<int:pk>', service_details, name='service-details'),
    path('project-details/<int:pk>', project_details, name='project-details'),
]
