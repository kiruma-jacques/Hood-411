from django import forms
from .models import Hood, Biz, member, Posts

class HoodCreateForm(forms.ModelForm):
    model=Hood
    exclude=['user']

class BizCreateForm(forms.ModelForm):
    model=Biz
    fields=('hood', 'name', 'description', 'category')

class HoodPostsForm(forms.ModelForm):
    model=Posts
    field=('post')
