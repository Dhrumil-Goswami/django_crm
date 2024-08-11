from django.urls import path
from agents import views

app_name = 'agents'

urlpatterns = [
    path('', views.AgentListView.as_view(), name="agents-list"),
    path('create/', views.AgentsCreateView.as_view(), name="agents-create"),
    path('<int:pk>/', views.AgentDetailView.as_view(), name="agents-details"),
    path('<int:pk>/update/', views.AgentUpdateView.as_view(), name="agents-update"),
    path('<int:pk>/delete/', views.AgentDeleteView.as_view(), name="agents-delete"),
]