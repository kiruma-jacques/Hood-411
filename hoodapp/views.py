from django.shortcuts import render
from .models import Hood,Biz,Member
# Create your views here.
def index(request):
    return render(request, 'index.html')
