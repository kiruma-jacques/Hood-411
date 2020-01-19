from django.shortcuts import render
from .models import Hood,Biz,Member,Posts
from .forms import HoodCreateForm,BizCreateForm,HoodPostsForm,ProfileUpdateForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    hoods = Hood.objects.all()
    return render(request, 'index.html',{'hoods':hoods})

def hood_details(request, id):
    details=Hood.objects.get(id=id)

    posts=Posts.objects.filter(hood=details)
    business=Biz.objects.filter(hood=details)

    create_post=HoodPostsForm(request.FILES,request.POST)
    biz_post=BizCreateForm(request.FILES,request.POST)
    if create_post.is_valid() and biz_post.is_valid():
        post=create_post.save(commit=False)
        post.user=request.user
        post.hood=details
        post.save()

        biz=biz_post.save(commit=False)
        biz.hood=details
        biz.save()
        return HttpResponseRedirect(request.path_info)
    else:
        create_post=HoodPostsForm()
        biz_post=BizCreateForm()

    return render(request, 'hood_detail.html', locals())

def search_biz(request):
    if request.method == "GET":
        search_term=request.GET.get('search')
        got_biz=Biz.objects.filter(name__icontains=search_term)[::-1]

        return render(request, 'results.html', locals())
    else:
        message="Looking for something, type it and hit search"
    return render(request, 'results.html', locals())

def myProfile(request,**kwargs):
    current_user=request.user
    prof_update=ProfileUpdateForm(request.POST)
    if prof_update.is_valid():
        profile=prof_update.save(commit=False)
        profile.user=current_user
        profile.save()
        return HttpResponseRedirect(request.path_info)
    else:
        prof_update=ProfileUpdateForm()
    return render(request, 'profile.html', locals())
