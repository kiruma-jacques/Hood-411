from django.shortcuts import render
from .models import Hood,Biz,Member
from .forms import HoodCreateForm,BizCreateForm,HoodPostsForm
# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    return render(request, 'index.html',{'hoods':hoods})

def hood_details(request, id):
    details=Hood.objects.get(id=id)
    return render(request, 'hood_detail.html', {'details':details})
