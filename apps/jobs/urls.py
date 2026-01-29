from django.urls import path
from .views import job_list_api
urlpatterns = [
     path('', job_list_api, name='job-list-api'),
]