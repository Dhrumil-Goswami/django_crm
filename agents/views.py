from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentsModelForm
from django.urls import reverse
from django.forms.models import BaseModelForm
from .mixins import OrganisorAndLoginRequiredMixin
from django.core.mail import send_mail


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'
    
    def get_queryset(self):
        user_profile_id = self.request.user.userprofile
        return Agent.objects.filter(user_profile_id=user_profile_id)
    
class AgentsCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentsModelForm 

    def get_success_url(self):
        return reverse("agents:agents-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.save()
        Agent.objects.create(
            user=user,
            user_profile_id=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent.',
            message='You were added as agent on crm .\n please come login to start working.',
            from_email= 'admin@test.com',
            recipient_list=[user.email]
        )
        return super(AgentsCreateView, self).form_valid(form) 
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)
    
class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agents_details.html"
    queryset = Agent.objects.all()
    context_object_name = "agent"

class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agents_update.html"
    queryset = Agent.objects.all()
    form_class = AgentsModelForm 

    def get_success_url(self):
        return reverse("agents:agents-list") 
    
class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agents_delete.html"
    form_class = AgentsModelForm
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agents-list") 
