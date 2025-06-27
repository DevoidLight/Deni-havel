from django import forms
from .models import BusinessIdea


class IdeaCreateForm(forms.ModelForm):
    class Meta:
        model = BusinessIdea
        fields = ('title', 'description', 'required_investment', 'business_plan')