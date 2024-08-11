from django import forms
from .models import Agent, Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
            'phone_number',
            'email',
            'converted_date',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField() 
    last_name = forms.CharField() 
    age = forms.IntegerField(min_value=0)
    phone_number = forms.IntegerField(min_value=0)
    email = forms.IntegerField(min_value=0)
    converted_date = forms.IntegerField(min_value=0)
    agent = forms.ModelChoiceField(queryset=Agent.objects.all())


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}
        

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(user_profile_id=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryForm(forms.ModelForm):
     class Meta:
        model = Lead
        fields = (
            'category',
        )