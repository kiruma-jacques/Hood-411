from django.shortcuts import render
from .models import Hood,Biz,Member
from .forms import HoodCreateForm,BizCreateForm,HoodPostsForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    return render(request, 'index.html',{'hoods':hoods})

def hood_details(request, id):
    details=Hood.objects.get(id=id)
    create_post=HoodPostsForm(request.FILES,request.POST)
    biz_post=BizCreateForm(request.FILES, request.POST)
    if create_post.is_valid() and biz_post.is_valid():
        post=create_post.save(commit=False)
        post.user=request.user
        post.hood=current_hood
        post.save()
        
        biz=biz_post.save(commit=False)
        biz.hood=current_hood
        biz.save()
        return HttpResponseRedirect(request.path_info)
    else:
        create_post=HoodPostsForm()
        biz_post=BizCreateForm()

    return render(request, 'hood_detail.html', locals())
