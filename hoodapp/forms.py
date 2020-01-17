from django import forms
from .models import Hood, Biz, member

class HoodCreateForm(forms.ModelForm):
    model=Hood
    exclude=['user']

class BizCreateForm(forms.ModelForm):
    model=Biz
    fields=('hood', 'name', 'description', 'category')
    
