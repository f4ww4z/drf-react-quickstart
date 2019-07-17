from django.urls import include, path
from leads.views import LeadListCreate

urlpatterns = [
    path('api/leads/', LeadListCreate.as_view()),
]
