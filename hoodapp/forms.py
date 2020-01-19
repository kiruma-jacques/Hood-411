from django import forms
from .models import Hood,Biz,Posts,Profile

class HoodCreateForm(forms.ModelForm):
    class Meta:
        model=Hood
        exclude=['user']

class BizCreateForm(forms.ModelForm):
    class Meta:
        model=Biz
        fields=('name', 'description')

class HoodPostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=('post',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
