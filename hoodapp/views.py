from django.shortcuts import render
from .models import Hood,Biz,Member
# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    return render(request, 'index.html',{'hoods':hoods})
