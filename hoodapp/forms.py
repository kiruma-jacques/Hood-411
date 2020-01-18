from django import forms
from .models import Hood,Biz,Posts

class HoodCreateForm(forms.ModelForm):
    class Meta:
        model=Hood
        exclude=['user']

class BizCreateForm(forms.ModelForm):
    class Meta:
        model=Biz
        fields=('hood', 'name', 'description', 'category')

class HoodPostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=('post',)
